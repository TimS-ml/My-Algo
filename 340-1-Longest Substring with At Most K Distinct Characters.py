# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/
# See 003 for template
# 相当于end指针就是len(s)
# 简单的无k版本


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str) -> int:
        dic = {}
        start = 0
        res = 0

        for i in range(len(s)):
            # initialize Hash
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

            while len(dic) > 2:
                temp = s[start]
                if dic[temp] > 1:
                    dic[temp] -= 1
                else:
                    del(dic[temp])  # delete the leftmost character
                start += 1
            res = max(res, i-start+1)
        return res


s1, k1 = "a", 0
s2, k2 = "eceba", 2

print(Solution().lengthOfLongestSubstringKDistinct(s2))
