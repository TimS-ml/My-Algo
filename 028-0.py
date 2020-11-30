# Brute Force

class Solution:
    def strStr(self, haystack, needle) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr2(self, haystack, needle) -> int:
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

    def strStr3(self, haystack, needle) -> int:
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
