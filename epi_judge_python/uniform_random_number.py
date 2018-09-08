import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random_rjimeno(lower_bound, upper_bound):
    randrange = upper_bound - lower_bound
    accumulator = 0
    for i in range(randrange):
        accumulator += zero_one_random()
    return accumulator + lower_bound


def uniform_random_book(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            # zero_one_random() is the provided random number generator.
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


uniform_random = uniform_random_book


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(lambda : [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound
             for a in result], upper_bound - lower_bound + 1, 0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("uniform_random_number.py",
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
