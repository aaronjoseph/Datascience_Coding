from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer list with 0's
        stack = []  # This stack will store indices of the temperatures list

        # Iterate over each temperature with its index
        for i, temp in enumerate(temperatures):
            # While there is at least one index on the stack and the current temperature
            # is greater than the temperature at that index:
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # The difference in days
            stack.append(i)  # Push the current day's index onto the stack

        return answer

# Example Usage:
solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# Expected Output: [1, 1, 4, 2, 1, 1, 0, 0]