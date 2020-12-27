# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


strs = ["cc", "c"]
# strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
