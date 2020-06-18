# https://leetcode-cn.com/problems/fibonacci-number/
# 0, 1, 1, 2


class Solution:
    def fib(self, N: int) -> int:
        cache = {}

        def recur(N):
            if N in cache:
                return cache[N]
            if N < 2:
                ans = N
            else:
                ans = recur(N - 1) + recur(N - 2)
            cache[N] = ans
            return ans

        return recur(N)


print(Solution().fib(4))
