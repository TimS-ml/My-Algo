# https://leetcode-cn.com/problems/pascals-triangle/
# zip version


class Solution(object):
    def generate(self, numRows):
        if not numRows:
            return []
        ans = [[1]]
        for i in range(numRows-1):
            ans.append([1] + [x+y for x, y in zip(ans[-1][:-1], ans[-1][1:])] + [1])
        return ans


print(Solution().generate(5))
