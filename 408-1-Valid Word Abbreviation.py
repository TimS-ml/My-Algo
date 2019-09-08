# https://leetcode-cn.com/problems/valid-word-abbreviation/


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        start = j = 0
        digit = False
        for i in range(0, len(abbr)):
            if abbr[i].isdigit():  # 直到走到不是.isdigit()
                if not digit:  # digit == False，2-3位数的第二位就已经是True了
                    if abbr[i] == "0":  # detail
                        return False
                    start = i
                    digit = True
            else:
                if digit:
                    jump = int(abbr[start:i])
                    # print(jump, start, i)
                    digit = False
                    j += jump
                if j >= len(word) or abbr[i] != word[j]:
                    return False
                j += 1
            if i == len(abbr) - 1:
                if digit:
                    jump = int(abbr[start:i+1])
                    digit = False
                    j += jump
                    if j != len(word):
                        return False
        return True


word = "internationalization"
abbr = "i12iz4n"
print(Solution().validWordAbbreviation(word, abbr))
