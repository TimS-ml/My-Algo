# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)  # column
        if m == 0:
            return False
        n = len(matrix[0])  # row
        if n == 0:
            return False

        # start with Bottom left
        i = m - 1  # label: [0, m-1]
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

target = 5

print(Solution().searchMatrix(matrix, target))
