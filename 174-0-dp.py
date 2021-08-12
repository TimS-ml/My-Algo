'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:

dp
[1] Base State
dp[i][j]: min health from (i, j) to end

why not: min health from start to (i, j)?
- because we have multiple path from (0, 0) to (i, j), 2 things to concern:
    - [a] sum of path value and [b] init value (depends on minimum value in the middle state)
    - i.e. a+b is the health remain at state (i, j)
        - and future steps may require bigger remain health
we can use dfs to solve multiple state issues

[2] State Transfer Equation
min(dp[i-1][j], dp[i][j-1])

[3] Initialize Conditions
dp[0][0] = dungeon[0][0]

[4] State Compression (optional)

[5] Terminate Conditions
'''

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        # at least one of them are 0
        # if row * col == 0:
        #     return sum([sum(row) for row in dungeon])
        BIG = float('inf')
        dp = [[BIG] * (col + 1) for _ in range(row + 1)]
        dp[row][col - 1] = dp[row - 1][col] = 1
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                Min = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(Min - dungeon[i][j], 1)

        return dp[0][0]



dungeon = [
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
]
print(Solution().calculateMinimumHP(dungeon))
