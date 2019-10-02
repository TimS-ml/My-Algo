# https://leetcode-cn.com/problems/valid-word-square/
# 1x1 为有效，例如[""]和["a"]
# 第一行和第一列不相同为无效
# 第一行和第一列若相同，检查子方块
# some error


class Solution:
    def check(self, matrix, n):
        j = n+1
        for i in range(n+1, len(matrix)):
            print(matrix[i][n], matrix[n][j])
            if matrix[i][n] != matrix[n][j]:
                return False
            j += 1
        return True

    def validWordSquare(self, words):
        for i in range(len(words)):
            if i == len(words[i])-1:
                break
            if self.check(words, i) == False:
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
