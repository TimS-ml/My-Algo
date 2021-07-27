# https://leetcode-cn.com/problems/pascals-triangle-ii/


class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        li1 = self.getRow(rowIndex - 1)
        li2 = [0] + li1[:-1]
        ans = [a + b for a, b in zip(li1, li2)]
        ans.append(li1[-1])
        return ans


print(Solution().getRow(5))
