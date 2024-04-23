'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    # brute force
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

            while y < len_y - 1 and x < len_x - 1:
                x += 1
                y += 1
                if matrix[y][x] != head:
                    return False

            if hy > 0:
                hy -= 1
            elif hx < len_x - 2:
                hx += 1
        return True

    # brute force
    def isToeplitzMatrix_2(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

    # case: matrix1
    # i=0
    # row[0][:-1]=[1, 2, 3]
    # row[1][1:]=[1, 2, 3]
    # i=1
    # row[1][:-1]=[5, 1, 2]
    # row[2][1:]=[5, 1, 2]
    def isToeplitzMatrix_3(self, matrix):
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
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
