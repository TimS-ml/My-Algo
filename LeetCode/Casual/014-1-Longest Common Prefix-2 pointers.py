# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        i = 0  # char pointer
        j = 0  # word pointer
        ans = 0  # the end point of common prefix
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]  # initialize char for first word
            else:
                if strs[j][i] != char:
                    break
            if j == len(strs) - 1:  # end of the word list
                i += 1  # move to next char
                j = 0  # reset
                ans += 1
            else:
                # char pointer: i-th char in word 0
                j += 1  # move word pointer
        return strs[j][:ans]


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
