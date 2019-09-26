# https://leetcode-cn.com/problems/implement-strstr/
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。
# 这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


class Solution:
    def strStr(self, haystack, needle) -> int:
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(0, len(haystack)):
            k = i
            j = 0
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == len(needle):
                return i
        return -1 if needle else 0


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
