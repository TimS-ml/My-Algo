# https://leetcode-cn.com/problems/climbing-stairs/


class Solution:
    def climb(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return Solution().climb(i + 1, n) + Solution().climb(i + 2, n)

    def climbStairs(self, n) -> int:
        return Solution().climb(0, n)


print(Solution().climbStairs(5))
