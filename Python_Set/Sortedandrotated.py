def check( nums):
    count_break = 0

    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            count_break += 1

    return count_break <= 1


nums = [3,4,5,1,2]
check(nums)
nums = [2,1,3,4]
check(nums)
