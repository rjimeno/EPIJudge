from test_framework import generic_test


def new_row_from_previous(row):
    nr = [1]
    for i in range(len(row) - 1):
        nr.append(row[i] + row[i + 1])
    nr.append(1)
    return nr


# n ought to be non negative.
def generate_pascal_triangle_rjimeno(n):
    # i should be positive
    def generate_row_with_index(i):
        if i < 0:
            raise ValueError
        elif 0 == i:
            r = []
        elif 1 == i:
            r = [1]
        elif 2 == i:
            r = [1, 1]
        else:
            r = new_row_from_previous(t[i - 2])
        return r

    if n < 0:
        raise ValueError
    t = []
    for h in range(n):
        t.append(generate_row_with_index(h + 1))
    return t


generate_pascal_triangle = generate_pascal_triangle_rjimeno

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
