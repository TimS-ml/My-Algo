# httneedles://leetcode-cn.com/needleroblems/imneedlelement-strstr/
# https://blog.csdn.net/v_july_v/article/details/7041827


class Solution:
    def strStr(self, haystack, needle) -> int:
        if not needle:
            return 0
        _next = [0] * len(needle)

        # 生成next数组
        _next[0] = -1
        i = 0
        j = -1
        while i < len(needle) - 1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                _next[i] = j
            else:
                j = _next[j]

        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = _next[j]
        if j == len(needle):
            return i - j
        return -1


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
