# https://leetcode-cn.com/problems/set-matrix-zeroes/
# 只保存要置零的行号和列号


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        front_col = False
        front_row = False
        len_col = len(matrix)  # 纵向
        len_row = len(matrix[0])  # 横向
        for i in range(len_col):
            if matrix[i][0] == 0:
                front_col = True  # 纵列里存在第一个数是0
            for j in range(len_row):
                if i == 0 and matrix[0][j] == 0:
                    front_row = True
                if i > 0 and j > 0 and matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0        
        
        for i in range(len_col):
            print(matrix[i])

        print(front_col, front_row)

        for i in range(len_col):
            if i > 0 and matrix[i][0] == 0:
                matrix[i] = [0] * len_row
            for j in range(len_row):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if front_col == True:
            for i in range(len_col):
                matrix[i][0] = 0
        if front_row == True:
            matrix[0] = [0] * len_row
        for i in range(len_col):
            print(matrix[i])



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

Solution().setZeroes(matrix3)
# Solution().setZeroes(matrix2)
