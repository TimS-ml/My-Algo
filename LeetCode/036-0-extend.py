'''
# Code Explain:
sol1 (loop once):
- Time complexity: O(1)
- Space complexity: O(1)


- how to convert to list
- how to find dupl
'''

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box1 = []
        box2 = []
        box3 = []
        for i in range(len(board)):
            # row and col
            row = [int(j) for j in board[i] if j != "."]
            col = [int(row[i]) for row in board if row[i] != "."]
            if len(set(row)) != len(row) or len(set(col)) != len(col):
                return False
            box1.extend([int(j) for j in board[i][0:3] if j != "."])
            box2.extend([int(j) for j in board[i][3:6] if j != "."])
            box3.extend([int(j) for j in board[i][6:9] if j != "."])
            if (i + 1) % 3 == 0:
                # duplicate in box
                if len(set(box1)) != len(box1) or \
                   len(set(box2)) != len(box2) or \
                   len(set(box3)) != len(box3):
                    return False
                box1 = []
                box2 = []
                box3 = []
        return True

    def isValidSudoku_2(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    # box_index:
                    #  1, 4, 7
                    #  2, 5, 8
                    #  3, 6, 9

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    if box_index == 0:
                        print(boxes[box_index], boxes)
                        # box[0] example: {3: 1, 8: 2, 6: 1, 9: 1}
                        # box example:
                        #   [{3: 1, 8: 2, 6: 1, 9: 1},
                        #    {7: 1, 1: 1, 9: 1, 5: 1},
                        #    {}, {}, {}, {}, {}, {}, {}]

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[
                            box_index][num] > 1:
                        return False

        return True

    def isValidSudoku_3(self, board: List[List[str]]) -> bool:
        box_index = [[], [], [], [], [], [], [], [], []]
        for i, x in enumerate(board):
            row = []
            if i % 3 == 0:
                col = [[], [], []]

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


board_1 = [[".", ".", ".", ".", ".", ".", "5", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["9", "3", ".", ".", "2", ".", "4", ".", "."],
           [".", ".", "7", ".", ".", ".", "3", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", "3", "4", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", "3", ".", ".", "."],
           [".", ".", ".", ".", ".", "5", "2", ".", "."]]

board_2 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board_3 = [["3", "8", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(board_1))
# print(Solution().isValidSudoku(board_2))
