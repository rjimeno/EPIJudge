import functools
import string
# Two lines above comes from EPIJudge solutions.
from test_framework import generic_test

# I have yet to write my solution as this one I copied from the book.

def convert_base_book(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


convert_base = convert_base_book


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
