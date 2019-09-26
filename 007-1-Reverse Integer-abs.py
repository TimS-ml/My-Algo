# https://leetcode-cn.com/problems/reverse-integer/


class Solution:
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)  # 返回绝对值
        ans = 0

        while x != 0:
            ans = ans * 10 + x % 10  # 注意溢出的问题
            x //= 10
            # print(ans)
        return ans * sign

        # if -2**31 < ans < 2**31 - 1:  # 判断是否越界
        #     return ans * flag
        # else:
        #     return 0


x1 = -123
x2 = 120
print(Solution().reverse(x2))
