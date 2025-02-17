def find_max_knapsack_profit(capacity, weights, values):
    # Number of items
    n = len(weights)

    # Create a DP table to store intermediate results
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    print(f"Initializing Knapsack DP Table with dimensions: {n+1} x {capacity+1}\n")

    # Iterate through each item
    for i in range(1, n + 1):
        print(f"\nConsidering item {i}: (Weight = {weights[i - 1]}, Value = {values[i - 1]})")

        for j in range(1, capacity + 1):
            print(f"  Checking knapsack capacity: {j}")

            # Check if the current item can fit in the current knapsack capacity
            if weights[i - 1] <= j:
                include_value = values[i - 1] + dp[i - 1][j - weights[i - 1]]
                exclude_value = dp[i - 1][j]

                print(f"    - Item can fit. Possible choices:")
                print(f"      ➤ Include: {values[i - 1]} + {dp[i - 1][j - weights[i - 1]]} = {include_value}")
                print(f"      ➤ Exclude: {exclude_value}")

                # Take the maximum value of including or excluding the item
                dp[i][j] = max(include_value, exclude_value)
                print(f"    ✅ Selecting maximum value: {dp[i][j]}")

            else:
                # If item can't fit, carry forward the previous max profit
                dp[i][j] = dp[i - 1][j]
                print(f"    ❌ Item too heavy, carrying forward value: {dp[i][j]}")

    print("\nFinal DP Table:")
    for row in dp:
        print(row)

    print(f"\n🎯 Maximum Knapsack Profit: {dp[-1][-1]}\n")
    return dp[-1][-1]  # [n][capacity]

# Example usage:
capacity = 7
weights = [2, 3, 4]
values = [6, 5, 7]

max_profit = find_max_knapsack_profit(capacity, weights, values)
