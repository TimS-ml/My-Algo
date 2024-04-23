
class Solution:
    # dp
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        lenPrices = len(prices)
        state = [0] * lenPrices
        for i in range(1, lenPrices):
            state[i] = max(state[i - 1] + prices[i] - prices[i - 1], 0)

        return max(state)
