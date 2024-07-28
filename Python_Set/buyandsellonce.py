prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]


def buy_and_sell(prices):
    min_price_so_far = float('inf')
    max_profit = 0.0

    for price in prices:
        max_profit_today = price - min_price_so_far
        max_profit = max(max_profit_today, max_profit)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit if max_profit > 0 else False

buy_and_sell(prices1)
buy_and_sell(prices2)