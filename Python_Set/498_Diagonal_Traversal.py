from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for k in range(m + n - 1):
            if k % 2 == 0:
                i = min(k, m - 1)
                j = k - i
                while i >= 0 and j < n:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                j = min(k, n - 1)
                i = k - j
                while j >= 0 and i < m:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1
        return result

x = Solution()
x.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])