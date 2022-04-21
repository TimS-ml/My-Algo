'''
O(log(min(m, n)))
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
            i = (l + r) // 2  # n1, mid
            j = half - i  # n2

            # what if out of bond?
            # n1l, n1r = n1[i], n1[i+1]
            n1l = n1[i] if i >= 0 else -float('INF')
            n1r = n1[i+1] if (i+1) < len(n1) else float('INF')
            n2l = n2[j] if i >= 0 else -float('INF')
            n2r = n2[j+1] if (j+1) < len(n1) else float('INF')
            
            # correct partitation, rule1 and rule2 both True
            if n1l <= n2r and n2l <= n1r:
                # odd
                if total % 2:
                    return min(n1r, n2r)
                # even
                else:
                    return (max(n1l, n2l) + min(n1r, n2r)) // 2
            # rule1 not True, n1[mid] > target 1
            elif n1l > n2r:
                r = i-1
            # rule2 not True, n1[mid+1] < target 2
            else n2l > n1r:
                l = i+1
