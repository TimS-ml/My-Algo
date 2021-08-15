'''
# Code Explain:
- Time complexity: O(klogN)
- Space complexity: O(N)

# Pros and Cons and Notation:

Each of the rows and columns are sorted in ascending order

归并排序
- 通过观察可以发现每一行每一列都是增序排列, 所以可以每次只加横行或者纵列
- 如何避免重复呢? 可以维持一个数组记录已经访问过的点
'''

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        # ans = None
        while k:
            ans, i, j = heapq.heappop(q)
            # if first col, go down
            if j == 0 and i + 1 < row:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            # go right
            if j + 1 < col:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
            k -= 1
        return ans


    def kthSmallest_2(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        q = [(matrix[i][0], i, 0) for i in range(row)]
        heapq.heapify(q)

        for _ in range(k - 1):
            num, x, y = heapq.heappop(q)
            if y != row - 1:
                heapq.heappush(q, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(q)[0]
