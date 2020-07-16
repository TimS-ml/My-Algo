# https://leetcode-cn.com/problems/add-bold-tag-in-string/
# official answer is not cool
# we can try KMP

import itertools


class Solution:
    def addBoldTag(self, s, dict) -> str:
        mark = [0] * len(s)

        def _trie():
            return collections.defaultdict(_trie)

        trie = _trie()
        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(s)
        for i in range(len(s)):
            curr = trie
            k = -1
            for j in range(i, len(s)):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if "_end" in curr:
                    k = j
            for j in range(i, k + 1):
                lookup[j] = True

        result = []
        for i in range(len(s)):
            if lookup[i] and (i == 0 or not lookup[i - 1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s) - 1 or not lookup[i + 1]):
                result.append("</b>")
        return "".join(result)


s = "abcxyz123"
dic = ["abc", "cxy", "3"]
print(Solution().addBoldTag(s, dic))
