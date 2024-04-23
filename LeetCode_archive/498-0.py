'''
# Code Explain:
- Time complexity: O(N) or O(ROW x COL)
- Space complexity: O(1)

A few things to start if you don't have a clue:
- We can turn zigzag traverse to single direction traverse
    - How the start point move? [ROW, 0] first, then [last ROW, COL], total ROW + COL - 1
    - Why '-1'? Because ROW and COL overlap at corner
- Total number of element: ROW x COL
- Total number of traverse: ROW + COL - 1
    - even idx: up right
    - odd idx: down left
- How to get r, c from current iter? Does r + c fixed?
    - For up right: row-- and col++
'''

from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ROW, COL = len(matrix), len(matrix[0])
        ans, traverse = [], []

        # total iter: row + col - 1
        for i in range(COL + ROW - 1):
            traverse.clear()
            # Elements in the first row and the last column are the respective heads.
            # r, c = 0 if i < COL else i - COL + 1, i if i < COL else COL - 1
            if i < COL:
                r = 0
                c = i
            else:
                r = i - COL + 1
                c = COL - 1

            while r < ROW and c > -1:
                traverse.append(matrix[r][c])
                r += 1
                c -= 1

            if i % 2 == 0:
                ans.extend(traverse[::-1])  # reverse
            else:
                ans.extend(traverse)
        return ans


    # to avoid traverse[::-1]
    def findDiagonalOrder_2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ROW, COL = len(matrix), len(matrix[0])
        ans = []

        for i in range(COL + ROW - 1):
            # Elements in the first row and the last column are the respective heads.
            r = 0 if i < COL else i - COL + 1
            c = i if i < ROW else ROW - 1

            if i % 2 == 1:
                for j in range(r, c + 1):
                    ans.append(matrix[j][i - j])  # reverse
            else:
                for j in range(c, r - 1, -1):
                    ans.append(matrix[j][i - j])
        return ans


    # Double loop is slow avoid using this solution
    def findDiagonalOrder_3(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ROW, COL = len(matrix), len(matrix[0])

        ans = []
        traverse = collections.defaultdict(list)

        for i in range(ROW):
            for j in range(COL):
                # Elements in the first row and the last column are the respective heads.
                traverse[i + j + 1].append(matrix[i][j])

        for i in sorted(traverse.keys()):
            if i % 2 == 1:
                traverse[i].reverse()  # reverse
            ans.extend(traverse[i])
        return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().findDiagonalOrder(matrix))
