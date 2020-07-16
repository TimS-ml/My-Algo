# https://leetcode-cn.com/problems/reverse-integer/


class Solution:
    def reverse(self, x):
        if x >= 0:
            ans = int(str(x)[-1::-1])
        else:
            ans = -int(str(x)[-1:0:-1])
        return ans if -2**31 < ans < 2**31 - 1 else 0


x1 = -123
x2 = 120
print(Solution().reverse(x1))
