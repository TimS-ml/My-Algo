# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/
# See 003 for template
# 根据答案改的，因为限制k distinct characters，双指针的想法比较自然
# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/solution/zhi-shao-bao-han-k-ge-bu-t


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0:
            return 0
        
        dic = {}
        start, end = 0, 0
        res = 0
        
        while end < len(s):
            # move end pointer
            dic[s[end]] = end
            end += 1

            # slidewindow contains 3 characters
            if len(dic) == k + 1:
                temp = min(dic.values())  # delete the leftmost character
                del dic[s[temp]]
                start = temp + 1  # move start pointer of the slidewindow
            res = max(res, end-start)
        return res


s1, k1 = "a", 0
s2, k2 = "eceba", 2

print(Solution().lengthOfLongestSubstringKDistinct(s2, k2))
