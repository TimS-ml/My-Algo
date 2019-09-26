# https://leetcode-cn.com/problems/string-to-integer-atoi/
# 不能判断带小数点的情况们
# if str.count('.') == 1:  # 小数有且仅有一个小数点

class Solution:
    def myAtoi(self, str) -> int:
        str = str.split(" ")
        # print(str)
        for i in range(len(str)):
            if str[i] != '':
                if len(str[i]) > 1 and str[i][0] == "-":
                    if str[i][1:].isdigit():
                        ans = -1 * int(str[i][1:])
                        print(ans)
                        if ans < -2**31:
                            return -2**31
                        return ans
                if str[i].isdigit():
                    ans = int(str[i])
                    # print(ans)
                    if ans > 2**31-1:
                        return 2**31-1
                    return ans
                else:
                    return 0
        return 0


s1 = "42"
s2 = "words and 987"
s3 = "   -42"
s4 = "4193 with words"
s5 = "-"
s6 = "  -0012a42"
s7 = "3.14159"  # output = 3
print(Solution().myAtoi(s7))
