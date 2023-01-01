'''
# Code Explain:
sol 1
- Time complexity: O(N)
- Space complexity: O(1)  # since they are both lowercase English letters only

- Time complexity: O(NlogN)
- Space complexity: O(1)  # no extra space, follow up: implement sort function
'''

import collections


class Solution:
    def isAnagram(self, s, t) -> bool:
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram_2(self, s, t) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t


# s = "anagram"
# t = "nagaram"
s = "aacc"
t = "ccac"
print(Solution().isAnagram(s, t))
