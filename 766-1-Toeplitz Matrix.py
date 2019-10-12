# https://leetcode-cn.com/problems/toeplitz-matrix/
# complex solution


class Solution:
    def isToeplitzMatrix(self, matrix):
        len_y = len(matrix)
        len_x = len(matrix[0])
        if len_y == 1:
            return True
        grid = len_x + len_y - 3  # ignore top-right and bottom-left

        hx, hy = 0, len_y - 2

        for i in range(grid):
            head = matrix[hy][hx]
            # print(head)
            x, y = hx, hy

            while y < len_y-1 and x < len_x-1:
                x += 1
                y += 1
                if matrix[y][x] != head:
                    return False

            if hy > 0:
                hy -= 1
            elif hx < len_x-2:
                hx += 1
        return True


matrix1 = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2],
]
matrix2 = [
    [1, 2],
    [2, 2],
]
print(Solution().isToeplitzMatrix(matrix2))
