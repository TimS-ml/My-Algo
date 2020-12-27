# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        ss = list(map(set, zip(*strs)))
        # [{'f'}, {'l', 'i'}, {'o', 'i', 'g'}, {'h', 'w', 'g'}]
        ans = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            ans = ans + x[0]
        return ans


strs = ["flower", "flow", "flight", "fight"]
print(Solution().longestCommonPrefix(strs))
