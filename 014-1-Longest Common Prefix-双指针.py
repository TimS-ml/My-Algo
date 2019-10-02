# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""

        i = 0
        j = 0
        end = 0
        while j < len(strs) and i < len(strs[j]):
            # j是单词编号，i是字母编号，用end来存储ans字母的位置
            if j == 0:
                char = strs[j][i]  # 首先设定为第一个词的第一个字母
                print('char', char)
            else:
                if strs[j][i] != char:  # 和第一个词的第i个字母（初始是第1个）比较一下
                    break

            if j == len(strs) - 1:  # 如果直到最后一个词的第i个字母也相等
                i += 1
                j = 0
                end += 1  # 最后一个相似字母的位置
            else:
                j += 1

        return strs[j][:end]


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
