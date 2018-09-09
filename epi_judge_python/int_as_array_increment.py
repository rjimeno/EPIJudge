from test_framework import generic_test


def plus_one(A):
    sa = ''.join(str(a) for a in A)
    na = int(sa)
    na += 1
    sa = str(na)
    al = [int(d) for d in sa]
    return al


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
