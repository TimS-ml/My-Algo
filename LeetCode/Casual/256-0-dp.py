'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[1] Base State
dp[i][j]: the minimum cost so far paint house i using color j
return min(dp[n-1])

[2] State Transfer Equation (important)
dp[i][j] = costs[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

[3] Initialize Conditions
dp[0][j] = costs[0][j]

[4] State Compression (optional)
[5] Terminate Conditions


# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        dp = [[float('inf') for _ in range(3)] for _ in range(n)]
        # init
        for j in range(3):
            dp[0][j] = costs[0][j]
        # transfer
        for i in range(1, n):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i - 1][(j + 1) % 3],
                                             dp[i - 1][(j + 2) % 3])
        return min(dp[n - 1])


c = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(c))
