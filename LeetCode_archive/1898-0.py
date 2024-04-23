'''
O(N log K)
N = len(s), K = len(removable)

binary search in 'removable'

isSubseq only got True or False
'''

class Solution:
    def maximumRemovals(self, s, p, removable):
        def isSubseq(s, subseq):
            i1, i2 = 0, 0

            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1

            return i2 == len(subseq)

        removed = set()
        res = 0
        l, r = 0, len(removable) - 1

        while l <= r:
            m = (l + r) // 2

            # take first m value from removable list
            removed = set(removable[:m + 1])
            if isSubseq(s, p):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1

        return res
