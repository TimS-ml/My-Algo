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
    # basic recursion
    def minimumTotal(self, triangle: List[List[int]]) -> int:

    def minimumTotal2(self, triangle: List[List[int]]) -> int:


t = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
print(Solution().minimumTotal2(t))

