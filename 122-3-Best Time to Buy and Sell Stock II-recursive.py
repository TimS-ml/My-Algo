import pandas as pd


class Solution:
    def maxProfit(self, prices):
        return Solution().calculate(prices, 0)

    def calculate(self, prices, s):
        if s >= len(prices): return 0
        max = 0
        for start in range(s, len(prices)):  # s~end
            maxprofit = 0
            for i in range(start + 1, len(prices)):
                if prices[start] < prices[i]:  # 一旦存在第s天之后的某天价格更高，就更新profit
                    # 比如len(prices) = 12，s = 3，5-12天范围内除了第6、7天之外都价格更高
                    # 那也就是分别尝试profit = (6-12天里的最大收益) + (第5天的时候买入的收益)，同理后面的几天
                    profit = Solution().calculate(prices, i + 1) + \
                        prices[i] - prices[start]
                    if profit > maxprofit:  # 更新这个range里的最大收益
                        maxprofit = profit
                if maxprofit > max:  # 更新全局最大收益
                    max = maxprofit
        return max


IN = [([7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]), ([1, 2, 3, 4, 5]), ([6, 1, 3, 2, 4, 7]), ([[5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]])]
useSet = 1
print(Solution().maxProfit(IN[useSet]))


