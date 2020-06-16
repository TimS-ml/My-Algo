# https://leetcode-cn.com/problems/most-common-word/

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.translate({ord(i): ' ' for i in '!?\',;.'})
        paragraph = paragraph.lower()
        dic = {}
        for n in paragraph.split(' '):
            dic[n] = dic.get(n, 0) + 1
        dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        print(dic)
        for i in dic:
            if i not in banned and i != '':
                return i


# p = "Bob hit a ball, the hit BALL flew far after it was hit."
# b = ["hit"]

# p = "a, a, a, a, b,b,b,c, c"
# b = ["a"]

p = "Bob. hIt, baLl"
b = ["bob", "hit"]
print(Solution().mostCommonWord(p, b))

