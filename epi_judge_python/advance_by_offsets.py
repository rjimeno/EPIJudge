from test_framework import generic_test

def can_reach_end_rjimeno(A):
    # The following value of A hangs my code:
    # A == [4, 3, 6, 0, 4, 9, 5, 6, 0, 2, 10, 6, 8, 8, 6, 5, 10, 7, 6, 2, 3, 10, 0, 2, 10, 4, 10, 9, 8, 3, 6, 4, 8, 2, 8, 8, 6, 3, 5, 3, 6, 6, 1, 6, 2, 7, 1, 1, 4, 4, 3, 7, 0, 4, 7, 10, 5, 8, 6, 7, 10, 0, 3, 4, 4, 4, 0, 3, 0, 1, 0, 1, 6, 6, 1, 7, 0, 6, 7, 10, 2, 2, 4, 10, 9, 8, 8, 5, 10, 5, 2, 5, 4, 3, 5, 7, 1, 8, 5, 8, 8, 0, 8, 7, 8, 10, 7, 8, 5, 1, 0, 9, 9, 7, 5, 2, 0, 1, 5, 7, 7, 4, 10, 10, 8, 8, 8, 5, 10, 6, 7, 4, 4, 9, 3, 1, 8, 6, 9, 1, 7, 10, 5, 9, 7, 1, 7, 0, 5, 1, 4, 8, 6, 8, 9, 3, 9, 3, 5, 8, 6, 1, 2, 7, 0, 2, 8, 2, 2, 2, 6, 6, 5, 2, 2, 1, 0, 7, 2, 4, 7, 9, 8, 8, 4, 8, 5, 5, 0, 2, 1, 4, 3, 2, 6, 1, 7, 1, 4, 7, 1, 2, 9, 5, 4, 0, 9, 3, 1, 9, 9, 5, 7, 5, 10, 5, 2, 1, 1, 6, 9, 1, 1, 1, 6, 10, 4, 10, 8, 1, 4, 8, 10, 3, 9, 9, 6, 5, 8, 3, 4, 10]
    outcome = False
    if 1 == len(A):
        outcome = True
    else:
        if 0 == A[0]:
            pass
        else:
            i = 0
            while i < A[0]:
                i += 1
                if can_reach_end(A[i:]):
                    outcome = True
                    break
                else:
                    pass
    return outcome

def can_reach_end_book(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

can_reach_end = can_reach_end_book
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
