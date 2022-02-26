# https://leetcode-cn.com/problems/longest-common-prefix/
# max(str) or min(str) depends on the order of ascII
# abb, aba, abac, max is abb, min is aba
# use chr(97) or ord('a')


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        s1 = min(strs)  # fight
        s2 = max(strs)  # flower
        for i, x in enumerate(s1):
            if x != s2[i]:  # if mismatch
                return s2[:i]
        return s1  # no mismatch for the (flower and flow) case


strs = ["flower", "flow", "flight", "fight"]
print(Solution().longestCommonPrefix(strs))
