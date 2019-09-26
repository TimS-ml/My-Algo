# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# some trick


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dic = {}
        # # res = 0
        # start = 0

        # for i in range(len(s)):
        #     if s[i] in dic:
        #         start = dic[s[i]] + 1
        #     dic[s[i]] = i  # initialize

        dic = {s[i] for i in range(len(s))}
        return dic


s1 = "abcabc"
s2 = "pwwkew"
print(Solution().lengthOfLongestSubstring(s2))
