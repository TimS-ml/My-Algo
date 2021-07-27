# https://leetcode-cn.com/problems/rotate-image/
# using [::-1] to flip the matrix upside down
# and then zip to transpose it


class Solution(object):
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        # no zip version, same as version 0
        # but flip first, transpose later
        # matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(Solution().rotate(matrix))
