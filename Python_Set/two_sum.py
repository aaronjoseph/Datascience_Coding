def two_sum(nums, target):
    num_map = {}  # Dictionary to store value -> index

    for i, num in enumerate(nums):
        complement = target - num  # Find the number needed to reach the target
        if complement in num_map:
            return [num_map[complement], i]  # Return stored index and current index
        num_map[num] = i  # Store the current number and its index

# Example Usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]