# https://leetcode-cn.com/problems/first-unique-character-in-a-string/
# ord 返回对应的 ASCII 数值，或者 Unicode 数值


class Solution:
    def firstUniqChar(self, s) -> int:
        # ans = ''.join(set(s))  # ''里面是字母之间的间隔，比如','
        letters = [0] * 26
        for c in s:  # 标记每个字母出现的次数
            ci = ord(c) - ord('a')
            letters[ci] += 1
        for i in range(0, len(s)):
            ci = ord(s[i]) - ord('a')
            if letters[ci] == 1:
                return i
        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))
