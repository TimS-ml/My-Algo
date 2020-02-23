# https://leetcode-cn.com/problems/implement-strstr/
# https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
# Sunday is easier to understand then KMP


class Solution:
    def getRight(self,str):
        n = len(str)
        if n <= 0:
            return []
        right = [-1 for i in range(256)]
        for i, c in enumerate(str):
            right[ord(c)] =  i
        return right

    def strStr(self, haystack, needle):
        right = self.getRight(needle)
        lenN = len(needle)
        lenH = len(haystack)
        i = 0
        while i <= lenH-lenN:
            j = lenN - 1
            while j >= 0:
                if haystack[i+j] != needle[j]:
                    if i+lenN < lenH:
                        skip = lenN - right[ord(haystack[i+lenN])]
                    else:
                        return -1
                    break
                j -= 1
            if j == -1:
                return i
            i += skip
        return -1


haystack = "hello"
needle = "ll"
# needle = ""
print(Solution().strStr(haystack, needle))
