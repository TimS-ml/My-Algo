# https://leetcode-cn.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s, t) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
