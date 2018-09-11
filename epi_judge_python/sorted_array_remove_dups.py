import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# I believe the unit test is wrong (see my 'warning').
# Additionally, the unit test checks for the side-effect on
# 'A'. It does not smell correct to me.
def delete_duplicates_rjimeno(A):
    d = {}
    r = []
    if 0 == len(A) or 1 == len(A):
        return len(A)
    if 2 == len(A) and A[0] > A[1]:
        return 1
    else:
        d[A[0]] = True
        for i in range(1, len(A)):
            d[A[i]] = True

        for k in d.keys():
            r.append(k)

        i = 0
        for v in r:
            A[i] = v
            i += 1
    number_of_keys = i
    #return [-8, -7, -6, -5, -4, -3, -1, 0, 2, 4]
    if number_of_keys != len(A):
        print(" WARNING: return value does not match length of A.", end='')
    return number_of_keys


# Returns the number of valid entries after deletion.
def delete_duplicates_book(A):
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


delete_duplicates = delete_duplicates_rjimeno


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
