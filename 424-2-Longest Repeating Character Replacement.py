# https://leetcode-cn.com/problems/longest-repeating-character-replacement/
# 需要替换的字符数目＝窗口字符数目－数量最多的字符数目
# 用子序列中出现频率最大的次数加上能被修改的次数K和窗口长度相比（也就是说窗口中都能统一）
# unfinish


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1

        for value, index in char_dict.items():
            char_dict[value] += 1
            res = max(res, char_dict[value])
            if res + k <= index - l:
                char_dict[s[l]] -= 1
                l += 1
        return res


s1, k1 = "ABAB", 2
s2, k2 = "AABABBA", 1
print(Solution().characterReplacement(s2, k2))
