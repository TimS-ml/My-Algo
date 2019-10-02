# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""

        ss = list(map(set, zip(*strs)))  # zip(*strs)
        print(ss)  # [{'f'}, {'l', 'i'}, {'o', 'i', 'g'}, {'h', 'w', 'g'}]，因为最短的flow是4个字母
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


strs = ["flower", "flow", "flight", "fight"]
print(Solution().longestCommonPrefix(strs))
