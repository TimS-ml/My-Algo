# https://leetcode-cn.com/problems/rotate-image/
# 2020 0425


class Solution(object):
    def rotate(self, matrix):
        ans = []
        for i in range(len(matrix)):
            ans.append([row[i] for row in matrix])
        for i in range(len(ans)):
            matrix[i] = ans[i][::-1]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(Solution().rotate(matrix))
