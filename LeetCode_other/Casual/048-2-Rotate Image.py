# https://leetcode-cn.com/problems/rotate-image/
# check bitwise operator '~'
# i + ~i = -1


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(int(n / 2)):
            for j in range(n - int(n / 2)):
                print(matrix[i][j], matrix[~j][i])
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

        # This is a longer version v2
        # if len(matrix) == 0:
        #     return

        # exchange = int(len(matrix)/2)
        # start = 0
        # end = len(matrix) - 1
        # x = start
        # y = end
        # exchange_range = len(matrix) - 1

        # for i in range(0, exchange):
        #     print('exchange_range', exchange_range)
        #     for j in range(0, exchange_range):
        #         matrix[start][x], matrix[x][end], matrix[end][y], matrix[y][start] = matrix[
        #             y][start], matrix[start][x], matrix[x][end], matrix[end][y]
        #         x += 1
        #         y -= 1

        #     exchange_range -= 2
        #     start += 1
        #     end -= 1
        #     x = start
        #     y = end

        # for i in range(len(matrix)):
        #     print(matrix[i])

        # This is a longer version
        # if len(matrix) == 0:
        #     return

        # exchange = int(len(matrix) / 2)
        # # print('exchange', exchange)
        # start = 0
        # end = len(matrix) - 1
        # a1, b1 = start, start
        # a2, b2 = start, end
        # a3, b3 = end, end
        # a4, b4 = end, start
        # # exchange_range = int(len(matrix) / 2) + 1
        # exchange_range = len(matrix) - 1

        # for i in range(0, exchange):
        #     print('exchange_range', exchange_range)
        #     for j in range(0, exchange_range):
        #         matrix[a1][b1], matrix[a2][b2], matrix[a3][b3], matrix[a4][b4] = matrix[a4][b4], matrix[a1][b1], \
        #             matrix[a2][b2], matrix[a3][b3]
        #         # print(matrix[a1][b1], matrix[a2][b2], matrix[a3][b3], matrix[a4][b4])
        #         b1 += 1
        #         a2 += 1
        #         b3 -= 1
        #         a4 -= 1
        #         # print(matrix[a1][b1], matrix[a2][b2], matrix[a3][b3], matrix[a4][b4])
        #     exchange_range -= 2
        #     start += 1
        #     end -= 1
        #     a1, b1 = start, start
        #     a2, b2 = start, end
        #     a3, b3 = end, end
        #     a4, b4 = end, start

        # for i in range(len(matrix)):
        #     print(matrix[i])


matrix1 = [
    [1, 2],
    [3, 4],
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matrix3 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

matrix4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

Solution().rotate(matrix2)
