# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# simple way to do this


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        start = 0

        for i in range(len(s)):
            if s[i] in dic:
                start = dic[s[i]] + 1
            dic[s[i]] = i

        for i in range(len(s)):
            res = max(res, i-start+1)
        return res


s1 = "abcabc"
s2 = "pwwkew"  # wke
print(Solution().lengthOfLongestSubstring(s2))
