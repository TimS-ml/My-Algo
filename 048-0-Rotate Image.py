# https://leetcode-cn.com/problems/rotate-image/


class Solution(object):
    def rotate(self, matrix):
        return


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# step1
# [3, 2, 1]
# [6, 5, 4]
# [9, 8, 7]

# step2
# 3 7 w-1-i = 2
# 2 4 w-1-i = 2
# 6 8 w-1-i = 1

# out
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

Solution().rotate(matrix)
