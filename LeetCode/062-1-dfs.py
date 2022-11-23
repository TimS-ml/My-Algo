'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

The number of possible paths the robot can take is then the binomial coefficient
C(m-1, m+n-2) = B(m+n-2,m-1) = factorial(m+n-2)/(factorial(m-1)*factorial(n-1))
Read as m-1 choose m+n-2
'''

from math import factorial
from functools import lru_cache


class Solution:
    # top-down (recursion)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths_2(self, m: int, n: int) -> int:
        return int(
            factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))

    # top-down (recursion + cache)
    def uniquePaths_3(self, m: int, n: int) -> int:
        cache = [[None for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            if i == 0 or j == 0:
                return 1
            if cache[j][i]:
                return cache[j][i]
            else:
                cache[j][i] = dfs(i - 1, j) + dfs(i, j - 1)
            return cache[j][i]

        return dfs(m - 1, n - 1)

    # brute force + lru
    def uniquePaths_4(self, m: int, n: int) -> int:
        @lru_cache()
        def dfs(i, j):
            if i == 0 or j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m - 1, n - 1)


m, n = 3, 7  # 28
print(Solution().uniquePaths(m, n))
