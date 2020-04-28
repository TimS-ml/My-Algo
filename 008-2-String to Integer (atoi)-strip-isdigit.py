# https://leetcode-cn.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, str) -> int:
        str = str.strip()  # 去除首尾空格
        print(str)
        sign = 1
        if not str:
            return 0
        if str[0] in ["+", "-"]:
            if str[0] == "-":
                sign = -1
            str = str[1:]
        ans = 0
        for c in str:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break
        ans *= sign
        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648
        return ans


s1 = "42"
s2 = "words and 987"
s3 = "   -42"
s4 = "4193 with words"
print(Solution().myAtoi(s4))
