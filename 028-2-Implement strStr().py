# https://leetcode-cn.com/problems/implement-strstr/
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。
# 这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


class Solution:
    def strStr(self, haystack, needle) -> int:
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i: i+len(needle)] == needle:
                # print(haystack[i: i+len(needle)])
                return i
        return -1


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
