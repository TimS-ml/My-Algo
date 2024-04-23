'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n^2)
- Space after optim: O(n)

- player picks either start or end
    -> remain a continue arr
    -> use start / stop to track position
- var `turn` change from +1 to -1, use sum to compare bigger or smaller
- assume each player plays to maximize his score

[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions



'''

from typing import List


class Solution:
    # bottom up
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0

    # space compress
    # dp[i][j] is calculated by dp[i+1][j] and dp[i][j-1]
    def PredictTheWinner_2(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [0] * length
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[length - 1] >= 0
