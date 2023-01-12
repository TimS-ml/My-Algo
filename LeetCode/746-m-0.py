'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

You can either start from the step with index 0, or the step with index 1.
Once you pay the cost, you can either climb one or two steps.
'''

from typing import List


class Solution:
    # dp[i] = min cost to 'reach' to i
    # dp[1] = min cost to reach 1 = 0
    # dp[4] = min cost to reach 4 = min(dp[3] + cost[3] or dp[2] + cost[2])
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        for i in range(2, len(cost)):
            oneStep = dp[i - 1] + cost[i - 1]
            twoStep = dp[i - 2] + cost[i - 2]
            dp[i] = min(oneStep, twoStep)

        oneStep = dp[-1] + cost[-1]
        twoStep = dp[-2] + cost[-2]
        ans = min(oneStep, twoStep)
        return ans 


c1 = [10,15,20]  # 15
c2 = [1,100,1,1,1,100,1,1,100,1]  # 6
print(Solution().minCostClimbingStairs(c1))
print(Solution().minCostClimbingStairs(c2))

