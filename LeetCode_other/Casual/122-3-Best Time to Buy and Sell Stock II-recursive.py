# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

import pysnooper


@pysnooper.snoop()
class Solution:
    def maxProfit(self, prices):
        return Solution().calculate(prices, 0)

    def calculate(self, prices, s):
        if s >= len(prices):
            return 0
        max = 0
        # slow pointer
        for start in range(s, len(prices)):  # day: s~end
            maxprofit = 0
            # fast pointer
            for i in range(start + 1, len(prices)):
                # update profit if day i prices is higher than day start
                if prices[start] < prices[i]:
                    # profit = (max profit from day i+1~end) + (buy at day i)
                    profit = Solution().calculate(prices, i + 1) + \
                        prices[i] - prices[start]
                    if profit > maxprofit:  # update max profit in range
                        maxprofit = profit
                if maxprofit > max:  # update global max profit
                    max = maxprofit
        return max


IN = [([7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]), ([1, 2, 3, 4, 5]),
      ([6, 1, 3, 2, 4, 7]), ([[5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]])]
useSet = 2
print(Solution().maxProfit(IN[useSet]))
