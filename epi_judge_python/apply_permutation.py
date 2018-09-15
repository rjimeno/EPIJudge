from test_framework import generic_test


def apply_permutation_rjimeno(perm, A):
    tmp = [0] * len(A)
    for i in range(len(perm)):
        tmp[perm[i]] = A[i]
    A[:] = tmp
    return A

def apply_permutation_book(perm, A):
    def cyclic_permutation(start, perm, A):
        i, temp = start, A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break
    for i in range(len(A)):
        # Traverses the cycle to see if i is the minumum element.
        j = perm[i]
        while j != i:
            if j < i:
                break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)


apply_permutation = apply_permutation_rjimeno

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
