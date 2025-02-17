def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)  # Step 1: Store all numbers in a set
    longest_streak = 0

    for num in num_set:  # Step 2: Iterate over unique numbers
        if num - 1 not in num_set:  # Step 3: Start a new sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:  # Step 4: Extend sequence
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)  # Step 5: Update max length

    return longest_streak

# Example Usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4 (Sequence: [1, 2, 3, 4])