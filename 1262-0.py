'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(nums) + 1)]
        dp[0][1] = -float('inf')
        dp[0][2] = -float('inf')
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                dp[i + 1][0] = max(dp[i][0], dp[i][0] + nums[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][1] + nums[i])
                dp[i + 1][2] = max(dp[i][2], dp[i][2] + nums[i])
            elif nums[i] % 3 == 1:
                dp[i + 1][0] = max(dp[i][0], dp[i][2] + nums[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][0] + nums[i])
                dp[i + 1][2] = max(dp[i][2], dp[i][1] + nums[i])
            else:
                dp[i + 1][0] = max(dp[i][0], dp[i][1] + nums[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][2] + nums[i])
                dp[i + 1][2] = max(dp[i][2], dp[i][0] + nums[i])
        return dp[-1][0]

    def maxSumDivThree_2(self, nums: List[int]) -> int:
        # max val for reminder == 0, 1, 2
        dp = [0] * 3
        for i in range(len(nums)):
            a = dp[0] + nums[i]
            b = dp[1] + nums[i]
            c = dp[2] + nums[i]
            dp[a % 3] = max(dp[a % 3], a)
            dp[b % 3] = max(dp[b % 3], b)
            dp[c % 3] = max(dp[c % 3], c)
        return dp[0]


#  nums = [1, 2, 3, 4, 4]
nums = [3, 6, 5, 1, 8]
