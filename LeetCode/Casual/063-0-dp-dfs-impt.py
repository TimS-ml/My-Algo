'''
# Code Explain:
- Time complexity: O(mn)
- Space complexity: O(mn)

[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:
take care on init process
'''

from typing import List


class Solution:
    # bottom-up
    # almost 70% of initialization...
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # special cases
        if (obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for row in range(m)]  # shape = m*n
        dp[0][0] = 1  # init
        # init edges
        for i in range(1, n):
            if (obstacleGrid[0][i] != 1):
                dp[0][i] = dp[0][i - 1]
        for j in range(1, m):
            if (obstacleGrid[j][0] != 1):
                dp[j][0] = dp[j - 1][0]
        # DP
        for x in range(1, m):
            for y in range(1, n):
                if (obstacleGrid[x][y] != 1):
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[-1][-1]

    # compress
    # compress makes init process easier
    # this is based on start and end on the diagonal
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # j=0, dp[0] = dp[0] + dp[-1]
        dp = [1] + [0] * n  # len = n+1
        for i in range(0, m):  # start at 0, not 1
            for j in range(0, n):
                # repeat m*n times
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        print(dp)
        return dp[-2]  # 0 ~ n-1

    # top-down
    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache()
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m - 1, n - 1)


# o = [[1]]
# o = [[1, 0]]
# o = [
#     [0,0],
#     [1,0]
# ]
o = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles2(o))
