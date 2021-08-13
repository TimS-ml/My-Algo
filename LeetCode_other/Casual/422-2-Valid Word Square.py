# https://leetcode-cn.com/problems/valid-word-square/
# 1x1 为有效, 例如[""]和["a"]
# 第一行和第一列不相同为无效
# 第一行和第一列若相同, 检查子方块


class Solution:
    def validWordSquare(self, words):
        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                if j >= len(words) or i >= len(
                        words[j]) or words[j][i] != words[i][j]:
                    return False
        return True


words1 = [
    "abcd",
    "bnrt",
    "crmy",
    "dtye",
]
words2 = [
    "ball",
    "area",
    "read",
    "lady",
]
words3 = [
    "ball",
    "asee",
    "lett",
    "le",
]
words4 = [
    "abcd",
    "bnrt",
    "crm",
    "dt",
]
print(Solution().validWordSquare(words3))
