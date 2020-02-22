# https://leetcode-cn.com/problems/implement-strstr/
# This barely finish the job


class Solution:
    def strStr(self, haystack, needle) -> int:
        lenH = len(haystack) 
        lenN = len(needle)
        if lenH == lenN:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(lenH):
            k = i
            j = 0
            while j < lenN and k < lenH and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == lenN:
                return i
        return -1 if needle else 0


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
