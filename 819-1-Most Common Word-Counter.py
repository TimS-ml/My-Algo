# https://leetcode-cn.com/problems/most-common-word/
# but this is slower

from typing import List
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower()
        count = collections.Counter(
            word for word in paragraph.lower().split()).most_common()
        for i in count:
            if i[0] not in banned:
                return i[0]


# p = "Bob hit a ball, the hit BALL flew far after it was hit."
# b = ["hit"]

# p = "a, a, a, a, b,b,b,c, c"
# b = ["a"]

p = "Bob. hIt, baLl"
b = ["bob", "hit"]
print(Solution().mostCommonWord(p, b))
