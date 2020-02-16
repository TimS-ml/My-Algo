# https://leetcode-cn.com/problems/diagonal-traverse/
# a faster version of version 1, no temp, and unnecessary yoperations
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        Y, X = len(matrix), len(matrix[0])
        ans = []

        for i in range(X + Y - 1):
            # Elements in the first row and the last column are the respective heads.
            r = 0 if i < X else i - X + 1
            c = i if i < Y else Y - 1

            if i % 2 == 1:
                for j in range(r, c+1):
                    ans.append(matrix[j][i-j])  # reverse
            else:
                for j in range(c, r-1, -1):
                    ans.append(matrix[j][i-j])
        return ans   


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix2 = [[2, 3]]
print(Solution().findDiagonalOrder(matrix2))
