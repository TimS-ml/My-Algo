# https://leetcode-cn.com/problems/roman-to-integer/

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 按照字符直接翻译，从M到I的顺序
# 做判断，如果L之后遇到I，则看2个字母，是否为IX
# 同理X之后遇到I也要判断（也就是各种if、and、or）
# 解答里面的方法更巧妙


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0

        if len(s) == 1:
            return d[s[0]]

        for i in range(0, len(s) - 1):
            c = s[i]
            c_after = s[i + 1]
            if d[c] < d[c_after]:  # 比如IX，d[c_after] = d[X]
                ans = ans - d[c]
            else:
                ans = ans + d[c]
        ans += d[s[-1]]  # 加上最后的一个数，是倒数第二个数的c_after
        return ans


s = "MCMXCI"  # 1994.M+CM+XC+IV = +1000 (-100 +1000) (-10 +100) (-1 +5)
print(Solution().romanToInt(s))
