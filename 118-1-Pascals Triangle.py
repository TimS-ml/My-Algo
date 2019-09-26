# https://leetcode-cn.com/problems/pascals-triangle/


class Solution(object):
    def generate(self, numRows):
        ans = [[1]*n for n in range(1, numRows+1)]  # 开数组
        for i in range(1, numRows+1):
            for j in range(0, i-2):  # 比如第三行只需要算1个数，rang(0, 1)
                ans[i-1][1+j] = ans[i-2][j] + ans[i-2][j+1]
                print(ans[i-1][1+j])
        return ans


print(Solution().generate(5))
