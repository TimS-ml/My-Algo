'''
# Code Explain:
- Time complexity: O(log(min(m, n)))
- Space complexity: O(1)

Binary search on sorter array
But this is an unnormal binary search...

Use two pointers merge 2 lists, O(N) time

The tricky part is to find the correct mid point!
[1] The mid point in merged list is at mid = (L1 + L2) // 2
[2] If without merge
    We will find two correct partiation such that
    p1 + p2 = mid, p1 >= 0, p2 >= 0
'''

class Solution:
    def findMedianSortedArrays(self, n1, n2):
        total = len(n1) + len(n2)
        half = total // 2

        # binary search on the sorter list (n1)
        if len(n2) < len(n1):
            n1, n2 = n2, n1

        l, r = 0, len(n1) - 1

        while True:
            # i + j = half - 2 = index sum
            i = (l + r) // 2  # n1, mid
            j = half - i - 2  # n2

            # what if out of bond?
            # n1l, n1r = n1[i], n1[i+1]
            n1l = n1[i] if i >= 0 else -float('INF')
            n1r = n1[i+1] if (i+1) < len(n1) else float('INF')
            n2l = n2[j] if j >= 0 else -float('INF')
            n2r = n2[j+1] if (j+1) < len(n2) else float('INF')

            # correct partitation, rule1 and rule2 both True
            if n1l <= n2r and n2l <= n1r:
                # odd
                if total % 2:
                    return min(n1r, n2r)
                # even
                else:
                    return (max(n1l, n2l) + min(n1r, n2r)) / 2
            # rule1 not True, n1[mid] > target 1
            elif n1l > n2r:
                r = i-1
            # rule2 not True, n1[mid+1] < target 2
            elif n2l > n1r:
                l = i+1

    def findMedianSortedArrays_2(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
