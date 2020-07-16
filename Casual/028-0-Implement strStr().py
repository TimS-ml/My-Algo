# https://leetcode-cn.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack, needle) -> int:
        lh, ln = len(haystack), len(needle)
        if ln > lh:
            return -1
        if ln == 0:
            return 0
        for i in range(lh - ln + 1):
            if haystack[i] == needle[0]:
                temp = haystack[i:i + ln]
                if temp == needle:
                    return i
        return -1


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
