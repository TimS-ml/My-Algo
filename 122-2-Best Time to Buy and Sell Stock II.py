# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
# Find peak and valley
# Which is quite annoying for the start and end points of data
# But actually this is slower...


class Solution:
    def maxProfit(self, prices):
        ans = 0
        valley = prices[0]
        peak = prices[0]

        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                valley = prices[i + 1]
            else:  # prices[i] < prices[i + 1]
                # small, large, small
                if i < len(prices) - 2 and prices[i + 1] >= prices[i + 2]:
                    peak = prices[i + 1]
                    ans += (peak - valley)
                if i >= len(prices) - 2:
                    peak = prices[i + 1]
                    ans += (peak - valley)
        return ans


IN = [([7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]), ([1, 2, 3, 4, 5]), ([6, 1, 3, 2, 4, 7]), ([[5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]])]
useSet = 1
print(Solution().maxProfit(IN[useSet]))
