# https://leetcode-cn.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        X, Y = len(matrix[0]), len(matrix)
        u, d, r, l = 0, Y-1, X-1, 0
        while d > u and r > l:
            ans.extend(matrix[u][j] for j in range(l, r))
            ans.extend(matrix[i][r] for i in range(u, d))
            ans.extend(matrix[d][j] for j in range(r, l, -1))
            ans.extend(matrix[i][l] for i in range(d, u, -1))
            u += 1
            d -= 1
            r -= 1
            l += 1
        if l == r:
            ans.extend(matrix[i][r] for i in range(u, d + 1))
        elif u == d:
            ans.extend(matrix[u][j] for j in range(l, r + 1))
        return ans


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(Solution().spiralOrder(matrix))
