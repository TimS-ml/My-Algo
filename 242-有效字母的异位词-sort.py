# https://leetcode-cn.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s, t) -> bool:
        if len(s) == len(t):
            s = list(s)
            t = list(t)
            s.sort()
            t.sort()
            # print(s, t)
            i = j = 0
            while i < len(t) and s[i] == t[j]:
                i += 1
                j += 1

            if j == len(t):
                return True
        return False


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
