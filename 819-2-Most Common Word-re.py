# https://leetcode-cn.com/problems/most-common-word/
# https://leetcode.com/problems/most-common-word/discuss/123854/C%2B%2BJavaPython-Easy-Solution-with-Explanation

from typing import List
import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        # words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        words = re.findall(r'\w+', paragraph.lower())
        print(words)
        return collections.Counter(w for w in words
                                   if w not in ban).most_common(1)[0][0]


# p = "Bob hit a ball, the hit BALL flew far after it was hit."
# b = ["hit"]

# p = "a, a, a, a, b,b,b,c, c"
# b = ["a"]

p = "Bob. hIt, baLl"
b = ["bob", "hit"]
print(Solution().mostCommonWord(p, b))
