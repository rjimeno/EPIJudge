from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string_rjimeno(x):
    if x < 0:
        sign = '-'
        x = -x
    elif 0 == x:
        return '0'
    else:
        sign = ''
    i_to_s = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    s = ''
    while 0 < x:
        s = i_to_s[x % 10] + s
        x //= 10
    s = sign + s
    return s


def string_to_int_rjimeno(s):
    if '-' == s[0]:
        sign = -1
        s = s[1:]
    else:
        sign = 1
    rs = s[::-1]
    s_to_i = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    tmp = 0
    for i in range(len(rs)):
        tmp += s_to_i[rs[i]] * 10 ** i
    tmp *= sign
    return tmp


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


int_to_string = int_to_string_rjimeno
string_to_int = string_to_int_rjimeno


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
