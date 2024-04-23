'''
# Code Explain:
- Time complexity: O(M+N)
- Space complexity: O(M+N)

lc 57 (insert + merge)
lc 987 (insert + intersection)

- l1 l2 already sorted
- l1 no internal intersections, l2 no internal interesction

case:
 (a, b) (c, d) (e, f)
    (x,          y)
return (x, b) (c, d) (e, y)
'''

from typing import List


class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        ans = []

        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            a1, a2 = l1[i][0], l1[i][1]
            b1, b2 = l2[j][0], l2[j][1]

            if b2 >= a1 and a2 >= b1:
                ans.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return ans

    def intervalIntersection_2(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest "endpoint"
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
