# https://leetcode-cn.com/problems/pascals-triangle-ii/


class Solution(object):
    def getRow(self, rowIndex):
        ans = [1]
        for i in range(rowIndex):
            ans = [sum(x) for x in zip(ans+[0], [0]+ans)]
        return ans

print(Solution().getRow(5))

