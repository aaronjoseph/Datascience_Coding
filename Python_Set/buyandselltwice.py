def buy_and_sell_stock_twice(prices):
    # Initialization
    max_total_profit = 0.0  # To store the maximum profit we can get
    min_price_so_far = float('inf')  # To store the minimum price encountered so far
    first_buy_sell_profits = [0] * len(prices)  # Array to store the maximum profit up to each day for the first transaction

    # Forward phase: For each day, calculate the maximum profit if we sell on that day
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)  # Update the minimum price so far
        max_total_profit = max(max_total_profit, price - min_price_so_far)  # Calculate profit if we sell today
        first_buy_sell_profits[i] = max_total_profit  # Store this profit in the array

    # Backward phase: For each day, calculate the maximum profit if we make the second buy on that day
    max_price_so_far = float('-inf')  # To store the maximum price encountered so far (from the end of the list)
    for i in reversed(range(1, len(prices))):  # Traverse from the end to the start
        max_price_so_far = max(max_price_so_far, prices[i])  # Update the maximum price so far
        # Calculate profit if we buy today and combine with the best profit we could have made by the first transaction
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - prices[i] + first_buy_sell_profits[i - 1]  # Profit from second transaction + first transaction
        )

    return max_total_profit

price = [3, 3, 5, 0, 0, 3, 1, 4]

print(buy_and_sell_stock_twice(price))