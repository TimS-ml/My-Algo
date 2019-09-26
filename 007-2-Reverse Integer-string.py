# https://leetcode-cn.com/problems/reverse-integer/
# Python字符串、整数、和浮点型数相互转换
# https://blog.csdn.net/huacode/article/details/79297329


class Solution:
    def reverse(self, x):
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = -int(str(x)[:0:-1])  # 0:-1 => 抛弃了开始的负号

        return ans
        # if -2 ** 31 < ans < 2 ** 31 - 1:
        #     return ans
        # else:
        #     return 0


x1 = -123
x2 = 120
print(Solution().reverse(x2))
