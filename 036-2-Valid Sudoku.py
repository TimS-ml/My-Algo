# https://leetcode-cn.com/problems/valid-sudoku/
# from typing import List, Any


class Solution:
    def isValidSudoku(self, board):
        box_index = [[], [], [], [], [], [], [], [], []]
        for i, x in enumerate(board):
            row = []
            if i % 3 == 0:
                col = [[], [], []]
            # else:
            #     print(col, i)

            for j, y in enumerate(x):
                if y == '.':
                    continue
                if y in row:
                    return False
                else:
                    row.append(y)
                flag = j // 3

                if y in box_index[j]:
                    return False
                else:
                    box_index[j].append(y)

                if y in col[flag]:
                    return False
                else:
                    col[flag].append(y)
        
        return True


board_1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board_2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(Solution().isValidSudoku(board_1))
# print(Solution().isValidSudoku(board_2))
