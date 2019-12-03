# https://leetcode-cn.com/problems/min-cost-climbing-stairs/


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        # f[i] = cost[i] + min(f[i+1], f[i+2])
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
            print(f1, f2)
        return min(f1, f2)


cost = [10, 15, 20]
print(Solution().minCostClimbingStairs(cost))
