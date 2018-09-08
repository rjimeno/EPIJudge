from test_framework import generic_test


def is_palindrome_number(x):
    xs = f"{x}"
    xr = xs[::-1]
    return xs == xr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
