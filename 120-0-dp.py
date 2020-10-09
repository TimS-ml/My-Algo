'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n^2)

[1] Base State
- triangle[i][j]: optimal path to row i col j
[2] State Transfer Equation
- triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + t[i][j]
[3] Initialize Conditions
- triangle[n][j] = t[n][j]
[4] State Compression (optional)
[5] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle)-1)):
            for j in range(i+1):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]

    # Space complexity: O(n)
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        dp = [0 for i in range(len(triangle)+1)]
        for i in reversed(range(len(triangle))):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        print(dp)
        return dp[0]


t = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
print(Solution().minimumTotal2(t))

