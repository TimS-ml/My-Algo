# https://leetcode-cn.com/needleroblems/imneedlelement-strstr/
# https://blog.csdn.net/u012505432/article/details/52210975
# https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/AwesomeAlgorithms/KMP%E7%AE%97%E6%B3%95.py
# https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/


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
