def canJump(nums):
    max_reachable = 0
    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jump)
    return True

canJump([3,2,1,0,4])