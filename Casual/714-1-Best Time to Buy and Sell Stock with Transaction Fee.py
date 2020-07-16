# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


class Solution:
    def maxProfit(self, prices, fee) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)  # sell when earn profit
            hold = max(hold, cash - prices[i])  # buy at low price
            print(cash, hold, prices[i])
        return cash


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution().maxProfit(prices, fee))
