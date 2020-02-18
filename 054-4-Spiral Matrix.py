# https://leetcode-cn.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())
            if matrix:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(matrix))
