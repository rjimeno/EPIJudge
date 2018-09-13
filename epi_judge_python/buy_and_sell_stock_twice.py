from test_framework import generic_test


def buy_and_sell_stock_once_book(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


def buy_and_sell_stock_twice_rjimeno(prices):
    days = len(prices)
    if 0 == days or 1 == days:
        profit = 0.0
    else:
        profit = float('-inf')
        profit = buy_and_sell_stock_once_book(prices)
        for i in range(days - 1):
            early_gain = buy_and_sell_stock_once_book(prices[:i + 1])
            late_gain = buy_and_sell_stock_once_book(prices[i + 1:])
            gain = early_gain + late_gain
            if profit < gain:
                profit = gain
    if profit < 0.0:
        profit = 0.0
    return profit


buy_and_sell_stock_twice = buy_and_sell_stock_twice_rjimeno


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
