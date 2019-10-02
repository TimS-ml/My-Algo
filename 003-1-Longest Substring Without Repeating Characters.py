# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 滑动窗口的templet，使用了Hash优化速度


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        start = 0

        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:  # show up second time
                start = dic[s[i]] + 1
            else:
                res = max(res, i-start+1)
            dic[s[i]] = i  # initialize
        return res


s1 = "abcabc"
s2 = "pwwkew"
print(Solution().lengthOfLongestSubstring(s2))
