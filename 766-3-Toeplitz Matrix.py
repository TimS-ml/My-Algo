# https://leetcode-cn.com/problems/toeplitz-matrix/
# same as solution 2

class Solution:
    def isToeplitzMatrix(self, matrix):
        tmp = []
        tmp2 = []
        for i in range(len(matrix)):
            if i == 0:
                tmp = matrix[i][:-1]
                tmp2 = matrix[i][:-1]
            else:
                tmp = matrix[i-1][:-1]
                tmp2 = matrix[i][1:]
            if tmp != tmp2:
                return(False)
        return(True)


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
