from typing import List
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of cumulative sums.
        sum_freq = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            count += sum_freq.get(current_sum - k, 0)
            sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
            print(current_sum, count, sum_freq)
        return count

# Example usage:
solution = Solution()
print(solution.subarraySum([1, 1,0,0, 1], k=2))  # Expected output: 2
