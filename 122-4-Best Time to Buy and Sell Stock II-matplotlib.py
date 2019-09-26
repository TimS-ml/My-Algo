import pandas as pd
import matplotlib.pyplot as plt


# 准备试试暴力算法，官网解答里面用了一种递归一样的方法实现的
# 20190201 - 我自己是想不出用递归来解决问题的……
# 顺便一说，range(s, len(prices))是不包括右边界的，也就是range(s, 12)是从s开始到11结束


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return Solution().calculate(prices, 0)

    def calculate(self, prices, s):
        if s >= len(prices):  # 递归的终止，最后一天到最后一天的利润是0
            return 0
        max = 0
        for start in range(s, len(prices)):  # 计算第s天到最后一天的收益
            maxprofit = 0
            for i in range(start + 1, len(prices)):
                if prices[start] < prices[i]:  # 一旦存在第s天之后的某天价格更高，就更新profit
                    # 比如len(prices) = 12，s = 3，5-12天范围内除了第6、7天之外都价格更高
                    # 那也就是分别尝试profit = (6-12天里的最大收益) + (第5天的时候买入的收益)，同理后面的几天
                    profit = Solution().calculate(prices, i + 1) + prices[i] - prices[start]
                    if profit > maxprofit:  # 更新这个range里的最大收益
                        maxprofit = profit
                if maxprofit > max:  # 更新全局最大收益
                    max = maxprofit
        return max


# 最终价格应该是12
prices = [7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4]
print(Solution().maxProfit(prices))


# df = pd.DataFrame({"prices": [7, 1, 5, 3, 6, 4, 2, 1, 5, 5, 6, 4],
#                    "date": pd.date_range('20190201', periods=12)},
#                    columns = ['prices','date'])
# print(df.head(12))

# pic = df[0:12]
# plt.plot(pic['date'], pic['prices'])
# # plt.xticks(rotation = 45)  # 旋转x轴刻度45度
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.xlabel('date')
# plt.ylabel('prices')
# plt.title('日期-价格 曲线')
# plt.show()
