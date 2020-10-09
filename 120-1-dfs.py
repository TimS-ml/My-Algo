'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n^2)

[1] Base State
- dp[i][j]: optimal path to row i col j
[2] State Transfer Equation
- dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + t[i][j]
[3] Initialize Conditions
- dp[n-1][j] = t[n-1][j]
- or outlier == 0
[4] State Compression (optional)
[5] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:
the difference between dp and dfs is:
dfs: top-down 
'''

from typing import List


class Solution:
    # basic recursion
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(i, j):
            if i == len(triangle):
                return 0
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]

        return dfs(0, 0)

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        cache = [[None for i in range(len(triangle))]
                 for j in range(len(triangle))]

        def dfs(i, j):
            if i == len(triangle):
                return 0
            if not cache[i][j]:
                cache[i][j] = min(dfs(i + 1, j), dfs(i + 1,
                                                     j + 1)) + triangle[i][j]
            return cache[i][j]

        return dfs(0, 0)


t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal2(t))
