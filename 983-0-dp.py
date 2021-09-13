'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
1 <= days.length <= 365
1 <= days[i] <= 365

if not travel in that day: dp[i]=dp[i+1]
'''

from typing import List
from functools import lru_cache


class Solution:
    # Use dp(i) to represent the money we need to spend from day i to the end of the year
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)

    # optimize dp(i+1) part in sol 1
    # Use dp(i) to represent the money we need to spend from day i to the end of the year
    def mincostTickets_2(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            ans = 10**9
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans

        return dp(0)

    # more intuitive
    # Use dp(i) to represent the money we need to spend from day 1 to day i
    def mincostTickets_3(self, days: List[int], costs: List[int]) -> int:
        # if days=[1,360], then len(dp)=361
        dp = [0 for _ in range(days[-1] + 1)]
        days_idx = 0

        for i in range(1, len(dp)):
            if i != days[days_idx]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        return dp[-1]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(Solution().mincostTickets(days, costs))
