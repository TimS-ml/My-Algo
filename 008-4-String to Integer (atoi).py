# https://leetcode-cn.com/problems/string-to-integer-atoi/
# https://leetcode-cn.com/problems/string-to-integer-atoi/solution/pythonchang-gui-jie-fa-by-jin407891080/


class Solution:
    def myAtoi(self, str) -> int:
        i, res, neg, over = 0, 0, False, (1 << 31) - 1
        while i < len(s) and s[i] == ' ': # ignore space first
            i += 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'): # save '-'
            neg = s[i] == '-'
            i += 1
        while i < len(s) and '0' <= s[i] <= '9': # generate number
            res = res * 10 + int(s[i])
            i += 1
        if res > over: # handle the overflow
            res = over + 1 if neg else over
        return -res if neg else res 


s1 = "42"
s2 = "words and 987"
s3 = "   -42"
s4 = "4193 with words"
s5 = "-"
s6 = "  -0012a42"
s7 = "3.14159"  # output = 3
print(Solution().myAtoi(s7))
