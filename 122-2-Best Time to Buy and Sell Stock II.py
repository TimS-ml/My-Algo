# 通过判断峰和谷来买买


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0

        maxprofit = 0
        valley = prices[0]
        peak = prices[0]

        for i in range(0, len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                valley = prices[i + 1]
            if prices[i] < prices[i + 1]:
                # 要用>=以包括price4里那种连续两个6的peak情况
                if i < len(prices) - 2 and prices[i + 1] >= prices[i + 2]:
                    peak = prices[i + 1]
                    maxprofit += (peak - valley)
                if i >= len(prices) - 2:  # 如过i是倒数1、2个数的话
                    peak = prices[i + 1]
                    maxprofit += (peak - valley)
                # print("valley = ", valley)
                # print("peak = ", peak)
                # print("\n")
        return maxprofit


# 最终价格应该是12
prices1 = [7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]

# 最终价格应该是4
prices2 = [1, 2, 3, 4, 5]

# 最终价格应该是7
prices3 = [6, 1, 3, 2, 4, 7]

# 最终价格应该是20
prices4 = [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]

print(Solution().maxProfit(prices4))
