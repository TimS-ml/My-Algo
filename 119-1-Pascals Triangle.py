# https://leetcode-cn.com/problems/pascals-triangle-ii/


class Solution(object):
    def getRow(self, rowIndex):
        ans = [1]*(rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                ans[j] += ans[j-1]
        return ans


print(Solution().getRow(5))

