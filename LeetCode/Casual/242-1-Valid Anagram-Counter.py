# https://leetcode-cn.com/problems/valid-anagram/
# unordered dict can use '==', interesting

import collections


class Solution:
    def isAnagram(self, s, t) -> bool:
        return collections.Counter(s) == collections.Counter(t)


# s = "anagram"
# t = "nagaram"
s = "aacc"
t = "ccac"
print(Solution().isAnagram(s, t))
