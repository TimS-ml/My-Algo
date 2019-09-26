# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/


class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        for i in range(0, len(prices)-1):
            for j in range(i, len(prices)):
                tmp = prices[j] - prices[i]
                if tmp > ans:
                    ans = tmp
        return ans


# prices = [7, 1, 5, 3, 6, 4]
prices = [2, 4, 1]
print(Solution().maxProfit(prices))
