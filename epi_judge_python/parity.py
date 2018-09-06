from test_framework import generic_test


def parity(natural):
    if natural == 0:
        parity = 0
    else:
        seen_ones = 0
        while natural > 0:
            seen_ones += natural % 2  # 1 when natural is odd
            natural = natural >> 1
        parity = seen_ones %2
    return parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
