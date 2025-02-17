from typing import List

def subarraySum( nums: List[int], k: int) -> int:
    ans, perfsum, d = 0, 0, {0: 1}

    for num in nums:
        perfsum += num

        if perfsum - k in d:
            ans += d[perfsum - k]

        d[perfsum] = d.get(perfsum, 0) + 1

    return ans

print(subarraySum(nums=[1,2,3], k=3))