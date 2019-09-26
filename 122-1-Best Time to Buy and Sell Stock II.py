# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices) -> int:
        if prices == []:
            return 0

        ans = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                ans += prices[i+1] - prices[i]
        return ans


# 最终价格应该是12
prices1 = [7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]

# 最终价格应该是4
prices2 = [1, 2, 3, 4, 5]

# 最终价格应该是7
prices3 = [6, 1, 3, 2, 4, 7]

# 最终价格应该是20
prices4 = [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]

print(Solution().maxProfit(prices2))
