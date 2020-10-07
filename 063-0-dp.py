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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if (obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for row in range(m)]
        dp[0][0] = 1
        # pay attention on init
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
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * n  # len = n+1
        for i in range(0, m):
            for j in range(0, n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[-2]


# o = [[1]]
o = [[1, 0]]
# o = [
#     [0,0],
#     [1,0]
# ]
# o = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
print(Solution().uniquePathsWithObstacles(o))
