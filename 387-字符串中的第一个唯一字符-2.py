# https://leetcode-cn.com/problems/first-unique-character-in-a-string/
# 参考HF python


class Solution:
    def firstUniqChar(self, s) -> int:
        letters = {}
        for c in s:  # 标记每个字母出现的次数
            letters.setdefault(c, 0)
            letters[c] += 1
        # print(letters)
        for i in range(0, len(s)):
            if letters[s[i]] == 1:
                return i
        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))
