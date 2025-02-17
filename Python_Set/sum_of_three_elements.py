import numpy as np
# nums = np.random.randint(low=0, high=1000, size = 20)
nums = np.random.choice(np.arange(1, 30), size=10, replace=False)

def sum_of_three_elements(nums, target):
    s_n = sorted(nums)

    for i in range(len(s_n)-2):
        l = i + 1
        r = len(s_n) -1

        while l < r:
            if target == s_n[l] + s_n[r] + s_n[i]:
                return True
            elif target > s_n[l] + s_n[r] + s_n[i]:
                l += 1
            else:
                r -= 1
    return False

print(nums)
sum_of_three_elements(nums, 20)

