from test_framework import generic_test


def buy_and_sell_stock_once_rjimeno(prices):
    days = len(prices)
    if 0 == days or 1 == days:
        profit = 0.0
    else:
        profit = -float('inf')
        low_price =  prices[0]
        for i in range(days - 1):
            buy_price = min(low_price, prices[i + 1])
            if buy_price < low_price:
                low_price = buy_price
            sell_price = max(prices[i + 1:])
            gain = sell_price - buy_price
            if profit < gain:
                profit = gain
    if profit < 0.0:
        profit = 0.0
    return profit


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
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


buy_and_sell_stock_once = buy_and_sell_stock_once_rjimeno


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
