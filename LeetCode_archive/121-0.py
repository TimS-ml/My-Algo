'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    # brute force
    def maxProfit(self, prices) -> int:
        ans = 0
        for i in range(0, len(prices) - 1):
            for j in range(i, len(prices)):
                tmp = prices[j] - prices[i]
                if tmp > ans:
                    ans = tmp
        return ans

    # 找到最小的谷之后的最大的峰
    # or you can treat this as dp with compression
    # or you can treat this as two pointers (minprice and i)
    def maxProfit_2(self, prices) -> int:
        ans = 0
        minprice = 999999
        for i in range(0, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice) > ans:
                ans = prices[i] - minprice
        return ans

    # dp
    def maxProfit_3(self, prices):
        if len(prices) <= 1:
            return 0

        # state is accumulate value
        state = [0] * len(prices)
        for i in range(1, len(prices)):
            state[i] = max(state[i - 1] + prices[i] - prices[i - 1], 0)

        return max(state)

# prices = [7, 1, 5, 3, 6, 4]
prices = [2, 4, 1]
print(Solution().maxProfit(prices))

