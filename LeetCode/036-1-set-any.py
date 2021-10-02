'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
'''

import collections


class Solution:
    def isValidSudoku(self, board):
        seen = set()
        return not any(x in seen or seen.add(x) for i, row in enumerate(board)
                       for j, c in enumerate(row) if c != '.'
                       for x in ((c, i), (j, c), (i / 3, j / 3, c)))

    def isValidSudoku_2(self, board):
        ans = []
        for i, row in enumerate(board):  # i是纵坐标, row是横向的数组
            for j, val in enumerate(row):  # j是横坐标, c是数值
                if val != '.':
                    # (i, val), (val, j)这种写法主要是为了把横纵坐标做区分
                    # (i // 3, j // 3, val)是类似于(x, y)这种坐标形式标注格子
                    ans += [(i, val), (val, j), (i // 3, j // 3, val)]
        return len(set(ans)) == len(ans)

        # seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
        #             for i, row in enumerate(board)
        #             for j, c in enumerate(row)
        #             if c != '.'), [])
        # return len(seen) == len(set(seen))

        # seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
        #             for i in range(9) for j in range(9)
        #             for c in [board[i][j]] if c != '.'), [])
        # return len(seen) == len(set(seen))

    def isValidSudoku_3(self, board):
        return 1 == max(
            list(
                collections.Counter(x for i, row in enumerate(board)
                                    for j, c in enumerate(row) if c != '.'
                                    for x in ((c, i), (j, c),
                                              (i / 3, j / 3, c))).values()) +
            [1])


board_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board_2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# print(Solution().isValidSudoku(board_1))
print(Solution().isValidSudoku(board_2))
