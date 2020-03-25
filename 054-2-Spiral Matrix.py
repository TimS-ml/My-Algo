# https://leetcode-cn.com/problems/spiral-matrix/
# this is a stupid official anster
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        X, Y = len(matrix[0]), len(matrix)
        seen = [[False] * X for i in matrix]
        ans = []
        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]
        row = col = 0
        move = 0

        for i in range(X * Y):
            ans.append(matrix[row][col])
            seen[row][col] = True
            cr, cc = row + drow[move], col + dcol[move]  # make a move
            if 0 <= cr < Y and 0 <= cc < X and not seen[cr][cc]:
                row, col = cr, cc
            else:
                move = (move + 1) % 4
                row, col = row + drow[move], col + dcol[move]

        return ans


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(Solution().spiralOrder(matrix))
