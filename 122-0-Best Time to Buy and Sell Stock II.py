# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                ans += prices[i] - prices[i - 1]
        return ans

 
IN = [([7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]), ([1, 2, 3, 4, 5]), ([6, 1, 3, 2, 4, 7]), ([[5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]])]
useSet = 1
print(Solution().maxProfit(IN[useSet]))

