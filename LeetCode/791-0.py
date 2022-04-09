'''
# Code Explain:
- Time complexity: O(len(order) + len(s))
- Space complexity: O(len((s)))

'''

import collections

class Solution(object):
    def customSortString(self, order, s):
        # freq dict of `target` (s)
        # s: char in order + char not in order
        count = collections.Counter(s)  
        ans = []

        # char in order
        for c in order:
            ans.append(c * count[c])
            count[c] = 0  # optional?

        # char not in order
        for c in count:
            ans.append(c * count[c])

        return ''.join(ans)

    def customSortString_2(self, order: str, s: str) -> str:
        dic = {v: k for k, v in enumerate(order)}  # index dict of `order`
        ans = sorted(s, key=lambda k: dic.get(k, len(s) + ord(k)))
        return ''.join(ans)
