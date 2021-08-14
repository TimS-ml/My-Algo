'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

- sum of positive = (total_sum - neg)
- target = sum of positive - neg
- neg = (total_sum - target) / 2 should be an integer

dp: dp[i][dp_sum] = num of ways: pick first i numbers, sum is dp_sum
    return answer is dp[n][neg]

init: 
- dp[0][0] = 1, consider no number, sum = 0
- dp[0][>0] = 0

transfer:
- dp_sum < nums[i], you cannot pick nums[i], dp[i][dp_sum] = dp[i-1][dp_sum]
- dp_sum >= nums[i], dp[i-1][dp_sum] + dp[i-1][dp_sum-nums[i]]
'''

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        diff = sum(nums) - target
        if diff < 0 or diff % 2 != 0:
            return 0

        L = len(nums)
        neg = int(diff / 2)

        dp = [[0] * (neg + 1) for _ in range(L + 1)]
        dp[0][0] = 1

        for i in range(1, L + 1):
            num = nums[i - 1]
            for dp_sum in range(neg + 1):
                dp[i][dp_sum] += dp[i - 1][dp_sum]
                if dp_sum >= num:
                    dp[i][dp_sum] += dp[i - 1][dp_sum - num]
        return dp[L][neg]
