# https://leetcode-cn.com/problems/pascals-triangle/


class Solution(object):
    def generate(self, numRows):
        ans = [[1] * (n + 1) for n in range(numRows)]
        for i in range(numRows):
            for j in range(0, i - 1):  # no need to calculate the edges
                ans[i][1 + j] = ans[i - 1][j] + ans[i - 1][j + 1]
        return ans


print(Solution().generate(5))
