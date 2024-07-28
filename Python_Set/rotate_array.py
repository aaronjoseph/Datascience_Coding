def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    steps = k % len(nums)
    nums[:] = nums[-steps:] + nums[:-steps]


arr = [1,2,3,4,5,6,7]

rotate(arr,3)