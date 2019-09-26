# https://leetcode-cn.com/problems/climbing-stairs/
# 跟动态规划一样的其实


class Solution:
    def climbStairs(self, n) -> int:
        if n == 1:
            return 1
        temp1 = 1
        ans = 2
        for i in range(3, n + 1):
            temp2 = temp1 + ans
            temp1 = ans
            ans = temp2
        return ans


print(Solution().climbStairs(5))
