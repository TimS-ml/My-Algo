# https://leetcode-cn.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s) -> int:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))
