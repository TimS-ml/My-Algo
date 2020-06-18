# https://leetcode-cn.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n) -> int:
        cache = {}

        def climb(i, n):
            if i in cache:
                return cache[i]
            if i > n:
                return 0
            if i == n:
                return 1
            else:
                ans = climb(i + 1, n) + climb(i + 2, n)
            cache[i] = ans
            return ans

        return climb(0, n)


print(Solution().climbStairs(5))
