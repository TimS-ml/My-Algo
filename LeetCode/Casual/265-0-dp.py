'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Check LC256
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
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        # init
        for j in range(k):
            dp[0][j] = costs[0][j]
        # transfer
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(
                    [dp[i - 1][(j + l) % k] for l in range(1, k)])
        return min(dp[n - 1])


# c = [[1, 5, 3], [2, 9, 4]]
# c = [[7, 6, 2]]
c = [[1, 3], [2, 4]]
print(Solution().minCostII(c))
