# https://leetcode-cn.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack, needle) -> int:
        return haystack.find(needle)


haystack = "hello"
needle = ""
# needle = ""
print(Solution().strStr(haystack, needle))
