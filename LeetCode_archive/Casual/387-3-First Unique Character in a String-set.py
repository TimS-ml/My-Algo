# https://leetcode-cn.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s) -> int:
        L = len(s)
        for i in set(s):
            if s.count(i) == 1:
                L = min(L, s.index(i))  # last element is s[len(s)-1] !
        return L if L != len(s) else -1


# s = "loveleetcode"
print(Solution().firstUniqChar(s))
