# https://leetcode-cn.com/problems/rotate-image/
# improve version of 2


class Solution(object):
    def rotate(self, matrix):
        if len(matrix) == 0:
            return

        exchange = int(len(matrix)/2)
        start = 0
        end = len(matrix) - 1
        x = start
        y = end
        exchange_range = len(matrix) - 1

        for i in range(0, exchange):
            print('exchange_range', exchange_range)
            for j in range(0, exchange_range):
                matrix[start][x], matrix[x][end], matrix[end][y], matrix[y][start] = matrix[y][start], matrix[start][x], matrix[x][end], matrix[end][y]
                x += 1
                y -= 1

            exchange_range -= 2
            start += 1
            end -= 1
            x = start
            y = end

        for i in range(len(matrix)):
            print(matrix[i])


matrix1 = [
    [1, 2],
    [3, 4],
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matrix3 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

matrix4 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

Solution().rotate(matrix4)
