# https://leetcode-cn.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, str) -> int:
        if len(str) == 0:
            return 0
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]
        ans, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            # ord return unicode of single char
            ans = ans * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ans, 2**31 - 1))


s = " "
# s = ""
# s = "-"
# s = "words and -987"
# s = "-91283472332"
# s = "-31words and -987"  # resturn 21
print(Solution().myAtoi(s))
