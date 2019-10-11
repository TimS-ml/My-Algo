# https://leetcode-cn.com/problems/01-matrix/
# Time limit exceed


class Solution:
    def updateMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = float('inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.dfs(i, j, matrix,0)
        return matrix
    
    def dfs(self, i, j, matrix, d):
        if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]<d:
            return
        matrix[i][j] = d
        self.dfs(i+1, j, matrix, d+1)
        self.dfs(i-1, j, matrix, d+1)
        self.dfs(i, j-1, matrix, d+1)
        self.dfs(i, j+1, matrix, d+1)


matrix1 = [
    [0,0,0],
    [0,1,0],
    [1,1,1]]

matrix2 = [
    [0,0,0],
    [0,2,0],
    [1,4,1]]

print(Solution().updateMatrix(matrix2))
