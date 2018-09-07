from test_framework import generic_test


def swap_bits_rjimeno(x, i, j):
    if i == j:
        return x
    mask = "0" * 64
    if i > j:
        i, j = j, i
    mask = mask[:i] + "1" + mask[i+1:j] + "1" + mask[j+1:]
    p = "{:064b}".format(x)
    p = p[::-1]
    q = p[:i] + p[j] + p[i+1:j] + p[i] + p[j+1:]
    q = q[::-1]
    print(mask[::-1] + " mask")
    return int(q, 2)


def swap_bits_book(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ.
    if (x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th bits differe. we will swap them by flipping their values.
        # Select the bits to flip with bit_mask. Since X^1 = 0 when x = 1 and 1
        # when x = 0, we can perform the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


swap_bits = swap_bits_rjimeno


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
