from test_framework import generic_test
import numpy as np


def rotate_matrix_rjimeno(square_matrix):
    if [] == square_matrix:
        return []
    m = np.array(square_matrix, int)
    m = np.rot90(m)
    m = np.rot90(m)
    m = np.rot90(m)
    m = m.tolist()
    square_matrix[:] = m[:]
    return


def rotate_matrix(square_matrix):
    # TODO - you fill in here.
    return

rotate_matrix = rotate_matrix_rjimeno

def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
