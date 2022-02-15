'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



dp[i][j] max Profit at day i
j = 0: not buy
j = 1: buy
'''


class Solution:
    def maxProfit(self, prices, fee) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)  # sell when earn profit
            hold = max(hold, cash - prices[i])  # buy at low price
            # print(cash, hold, prices[i])
        return cash

    def maxProfit_dp(self, prices, fee) -> int:
        # dp = [[-1 for j in [0, 1]] for j in range(len(prices))]
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]  # buy
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

    def maxProfit_dp_2(self, prices, fee) -> int:
        size = len(prices)
        if size < 2:
            return 0

        # 规定在买入股票的时候扣除手续费
        dp = [0, 0]
        dp[0] = 0
        dp[1] = -prices[0] - fee
        for i in range(1, size):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], dp[0] - prices[i] - fee)
        return dp[0]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution().maxProfit_dp(prices, fee))
