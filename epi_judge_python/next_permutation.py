from test_framework import generic_test


# Not working at all; just a starting point.
def next_permutation_rjimeno(perm):
    def longest_decreasing_suffix(perm):
        l = len(perm)
        if 0 == l:
            raise ValueError
        elif 1 == l:
            pass
        elif 2 <= l:
            p = l - 2
            while 0 <= p and perm[p] >= perm[p + 1]:
                p -= 1
            if -1 == p:
                # That was the "last" permutation.
                pass  # TODO: find out what to do.
                # Should we return a special value to indicate the above?
        return p  # Return the "pivot".

    # TODO - you fill in here.
    decrease_after = longest_decreasing_suffix(perm)
    print(f"decrease_after = {decrease_after}.")
    return []


def next_permutation_book(perm):
    # Find the first entry from the right that is smaller than the entry
    # immediately after it
    inversion_point = len(perm) - 2
    while (inversion_point >= 0
           and perm[inversion_point] >=  perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the last permutation.

    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion point, if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply reverse these entries to get the smallest dictionary order.
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


next_permutation = next_permutation_book


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
