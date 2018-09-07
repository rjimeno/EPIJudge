from test_framework import generic_test


def reverse_bits_rjimeno(x):
    xb = "{:064b}".format(x)
    xbr = xb[::-1]
    return int(xbr, 2)


reverse_bits = reverse_bits_rjimeno


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
