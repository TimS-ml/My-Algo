# https://leetcode-cn.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s) -> int:
        for i, ch in enumerate(s):
            if ch not in s[:i]+s[i+1:]:
                return i
        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))
