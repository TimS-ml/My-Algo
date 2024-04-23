'''
# Code Explain:
for rolling
- Time complexity: O(N)
- Space complexity: O(1)

You can either start from the step with index 0, or the step with index 1.
Once you pay the cost, you can either climb one or two steps.

dp[i] = min cost to climb to i
cost >= 0
'''


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        dp[1] = cost[0]
        dp[2] = cost[1]

        # bottom up
        # dp[i] <-> cost[i-1]
        for i in range(3, len(cost) + 1):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i-1]

        return min(dp[-1], dp[-2])

    def minCostClimbingStairs_mod(self, cost: List[int]) -> int:
        # rolling
        first = cost[0]
        second = cost[1]

        # bottom up
        #      old 1st
        # 1st  old 2nd
        # 2nd
        for i in range(3, len(cost) + 1):
            old_f, old_s = first, second
            first = old_s
            second = min(old_f, old_s) + cost[i-1]

        return min(first, second)


    def minCostClimbingStairs_2(self, cost: List[int]) -> int:
        # top down
        # dp[i] <-> cost[i-1]
        cache = {}
        def helper(idx):
            if idx <= 2:
                return cost[idx-1]

            if idx in cache:
                return cache[idx]

            ans = min(helper(idx-1), helper(idx-2)) + cost[idx-1]
            cache[idx] = ans
            return ans

        return min(helper(len(cost)), helper(len(cost)-1))
