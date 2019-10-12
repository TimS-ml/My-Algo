# https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        res = 0
        start = 0

        for i in range(len(s)):
            # initialize Hash
            dic[s[i]] = i
            # slidewindow contains 3 characters
            if len(dic) == 3:
                temp = min(dic.values())  # delete the leftmost character
                del dic[s[temp]]
                start = temp + 1  # move start pointer of the slidewindow
            res = max(res, i-start+1)
        return res
