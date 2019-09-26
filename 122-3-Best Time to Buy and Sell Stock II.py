# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# 区别在于可以多次买卖


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i - 1]:
        #         ans += prices[i] - prices[i - 1]
        # return ans

        for i in range(0, len(prices) - 1):  # 不包括最后一个元素
            if prices[i] < prices[i + 1]:
                ans += prices[i + 1] - prices[i]
        return ans


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
