# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/


# 找到最小的谷之后的最大的峰
class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        minprice = 999999
        for i in range(0, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice) > ans:
                ans = prices[i] - minprice
        return ans


# prices = [7, 1, 5, 3, 6, 4]
prices = [2, 4, 1]
print(Solution().maxProfit(prices))
