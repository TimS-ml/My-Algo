# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/
# See 003 for template
# 相当于end指针就是len(s)


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = {}
        start = 0
        res = 0

        for i in range(len(s)):
            # initialize Hash
            dic[s[i]] = i
            # slidewindow contains 3 characters
            if len(dic) == k + 1:
                temp = min(dic.values())  # delete the leftmost character
                del dic[s[temp]]
                start = temp + 1  # move start pointer of the slidewindow
            res = max(res, i - start + 1)
        return res


s1, k1 = "a", 0
s2, k2 = "eceba", 2

print(Solution().lengthOfLongestSubstringKDistinct(s2, k2))
