# https://leetcode-cn.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, str) -> int:
        L = len(str)
        ans = ''
        for i in range(L):
            if str[i] == ' ':
                continue
            elif (i != L - 1 and str[i + 1].isnumeric() and
                  (str[i] == '+' or str[i] == '-')) or str[i].isnumeric():
                ans = str[i]
                for j in range(i + 1, L):
                    if str[j].isnumeric():
                        ans += str[j]
                    else:
                        break
                ans = int(ans)
                if -2**31 < ans < 2**31 - 1:
                    return ans
                elif ans > 0:
                    return 2**31 - 1
                else:
                    return -2**31
            else:
                return 0
        return 0


s = " "
# s = ""
# s = "-"
# s = "words and -987"
# s = "-91283472332"
# s = "-31words and -987"  # resturn 21
print(Solution().myAtoi(s))
