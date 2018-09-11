from test_framework import generic_test

# Feels like it hangs when trying to process a list of 1*10**5 (or so)prices
def buy_and_sell_stock_once_rjimeno_brute_force(prices):
#    print(f" prices == {prices} ", end='')
    if len(prices) < 2:
        return 0.0
    best_i = 0
    best_j = 1
    best_gain = 0
    i = 0
    while i < len(prices) - 1:
        j = i + 1
        while j < len(prices):
            this_gain = prices[j] - prices[i]
            if  this_gain > best_gain:
                best_gain = this_gain
                best_i = i
                best_j = j
            j += 1
        i += 1
    return best_gain


def buy_and_sell_stock_once_book(prices):
    # code goes here
    return 0.0


buy_and_sell_stock_once = buy_and_sell_stock_once_rjimeno_brute_force


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
