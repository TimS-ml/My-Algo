'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(logN)

- n is odd
- n is even
- n < 0
'''


class Solution:
    # dfs
    # top down
    def myPow(self, x: float, n: int) -> float:
        cache = {}

        def Pow(x, i):
            if i in cache:
                return cache[i]
            if i <= 2:
                return x**i
            else:
                cache[i] = Pow(x, int(i / 2)) * Pow(x, i - int(i / 2))
            return cache[i]

        return Pow(x, n)

    # dp
    # bottom up
    def myPow_2(self, x: float, n: int) -> float:
        dp = [1] + [x] + [None] * (n - 1)
        for i in range(1, n + 1):
            dp[i] = dp[int(i / 2)] * dp[i - int(i / 2)]
        return dp[n]


x, n = 2, 10
print(Solution().myPow2(x, n))
