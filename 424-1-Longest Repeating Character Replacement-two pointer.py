# https://leetcode-cn.com/problems/longest-repeating-character-replacement/
# k ＝ window size － 数量最多的字符数目


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        l = 0
        res = 0
        for i in range(len(s)):
            char_dict[s[i]] = char_dict.get(s[i], 0) + 1
            max_letter = max(char_dict, key=char_dict.get)
            # 如果替换的字符数目超过给定的k，则移动左边界
            while i-l+1-char_dict[max_letter] > k:
                char_dict[s[l]] -= 1
                l += 1
                # 需要更新最多个数的字符
                max_letter = max(char_dict, key=char_dict.get)
            # 如果s[i] 超出了替换的字符数目，需要先处理，再计算结果
            res = max(res, i-l+1)
        return res


s, k = "ABAB", 2
s2, k2 = "AAABACA", 1
print(Solution().characterReplacement(s2, k2))
