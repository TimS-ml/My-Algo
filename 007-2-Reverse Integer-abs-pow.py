# https://leetcode-cn.com/problems/reverse-integer/
# max_int and min_int is more readable


class Solution:
    def reverse(self, x):
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)

        str_x = str(abs(x))
        str_x_reversed = str_x[::-1]
        result = int(str_x_reversed)
        result = result * -1 if x < 0 else result

        return result if (result < max_int and result > min_int) else 0


x1 = -123
x2 = 120
print(Solution().reverse(x2))
