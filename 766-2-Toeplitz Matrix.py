# https://leetcode-cn.com/problems/toeplitz-matrix/


class Solution:
    def isToeplitzMatrix(self, matrix):
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        for i in range(len(matrix)-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True


matrix1 = [
    [1,2,3,4], 
    [5,1,2,3], 
    [9,5,1,2],
]
matrix2 = [
  [1,2],
  [2,2],
]
print(Solution().isToeplitzMatrix(matrix2))
