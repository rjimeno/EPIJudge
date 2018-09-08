from test_framework import generic_test


def weight(i):
    ib = "{:b}".format(i)
    weight = 0
    for v in ib:
        weight += int(v)
    return weight


def closest_int_same_bit_count(x):
    wx = weight(x)
    i = 1
    while True:
        if weight(x + i) == wx:
            closest = x + i
            break
        elif weight(x - i) == wx:
            closest = x - i
            break
        i += 1
    return closest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
