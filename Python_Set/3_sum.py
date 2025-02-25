from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        len_array = len(nums)

        for i in range(len_array - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len_array - 1

            while left < right:
                summation = nums[i] + nums[left] + nums[right]

                if summation < 0:
                    left += 1
                elif summation > 0:
                    right -= 1

                else:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                left += 1
                right -= 1

        return res


nums = [-4, -2, -2, -2, -1, 0, 1, 1, 2, 4]
x = Solution()
x.threeSum(nums)