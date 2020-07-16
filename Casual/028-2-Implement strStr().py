# https://leetcode-cn.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack, needle) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
