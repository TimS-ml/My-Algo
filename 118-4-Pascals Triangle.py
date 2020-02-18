# https://leetcode-cn.com/problems/pascals-triangle/
# fastest version, similar as version 3


class Solution(object):
    def generate(self, numRows):
        ans = []
        temp = [1]
        for i in range(numRows):
            ans.append(temp)
            temp = [1] + [temp[i]+temp[i+1] for i in range(len(temp)-1)] + [1]
        return ans


print(Solution().generate(5))
