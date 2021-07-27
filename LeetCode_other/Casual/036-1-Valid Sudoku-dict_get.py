# https://leetcode-cn.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    # print(i, j, box_index)
                    # box_index分布：
                    #     1, 4, 7
                    #     2, 5, 8
                    #     3, 6, 9

                    # keep the current cell value
                    # get(num, 0)，0的作用是初始化，用过一次就没用了
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(
                        num, 0) + 1  # 在相同的box[box_index]下寻找是否有同数值的元素
                    if box_index == 0:
                        print(boxes[box_index], boxes)
                        # box[0]的样子：{3: 1, 8: 2, 6: 1, 9: 1}
                        # box的样子：[{3: 1, 8: 2, 6: 1, 9: 1}, {7: 1, 1: 1, 9: 1, 5: 1}, {}, {}, {}, {}, {}, {}, {}]

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[
                            box_index][num] > 1:
                        return False

        return True


board_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board_2 = [["3", "8", ".", ".", "7", ".", ".", ".", "."],
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
