from test_framework import generic_test


NOT = 0
TTB = +1
BTT = -1
LTR = TTB
RTL = BTT

delta_r = TTB
delta_c = LTR

# WORK IN PROGRESS.
def matrix_in_spiral_order_rjimeno(square_matrix):
    if [] == square_matrix:
        return []
    # square_matrix must be "square"; otherwise this will probably fail.
    output = []
    rl, rh = 0, len(square_matrix)
    cl, ch = rl, rh
    r = rl
    c = cl
    while rl <= r and r < rh:
        print()
        print("square_matrix[{}] == [ ".format(r), end='')
        if c < rh:
            delta_c = LTR
        else:
            delta_c = RTL
            c += delta_c
        while cl <= c and c < ch:
            print("{} ".format(square_matrix[r][c]), end='')
            output.append(square_matrix[r][c])
            c += delta_c
        print("]")
        r += delta_r
    # TODO - you fill in here.
    return output


def matrix_in_spiral_order_book(square_matrix):
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(
            square_matrix[-1 -offset][-1 - offset:offset:-1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

matrix_in_spiral_order = matrix_in_spiral_order_book

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
