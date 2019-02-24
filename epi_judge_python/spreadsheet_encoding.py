import functools
# The line above comes from EPIJudge solutions.
from test_framework import generic_test

# I have yet to write my solution as this one I copied from the book.

#def ss_decode_col_id(col):
    # TODO - you fill in here.

#    return accumulator

def ss_decode_col_id_book(col):

    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)

ss_decode_col_id = ss_decode_col_id_book

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
