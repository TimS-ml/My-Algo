# https://leetcode-cn.com/problems/set-matrix-zeroes/
# 只保存要置零的行号和列号


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        front_col = False
        len_col = len(matrix)  # 纵向
        len_row = len(matrix[0])  # 横向
        for i in range(len_col):
            if matrix[i][0] == 0:
                front_col = True  # 纵列里存在第一个数是0
            for j in range(1, len_row):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in reversed(range(len_col)):
            for j in reversed(range(1, len_row)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if front_col:
                matrix[i][0] = 0


matrix1 = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
]

matrix2 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
]

matrix3 = [[1, 0]]

matrix4 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5],
]

# Solution().setZeroes(matrix3)
Solution().setZeroes(matrix4)
