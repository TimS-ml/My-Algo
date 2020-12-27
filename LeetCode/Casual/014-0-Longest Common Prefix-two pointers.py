# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        zipped = zip(*strs)
        ans = 0
        for i in zipped:
            print(i)
            if len(set(i)) != 1:
                return strs[0][:ans]
            ans += 1
        return strs[0][:ans]


strs = ["cc", "c"]
# strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
