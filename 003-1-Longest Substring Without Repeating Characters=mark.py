# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# combine hash and compare in one loop


# Initialize Hash dict

# [1] return a set
# dic = {s[i] for i in range(len(s))}

# [2] return a dict
# dic = {}
# start = 0
# for i in range(len(s)):
#     if s[i] in dic:
#         start = dic[s[i]] + 1
#     dic[s[i]] = i


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
s2 = "pwwkew"  # wke
print(Solution().lengthOfLongestSubstring(s2))
