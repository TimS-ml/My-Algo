# https://leetcode-cn.com/problems/two-sum-less-than-k/

from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        L = len(A)
        A.sort()
        if L < 2 or A[0] > K:
            return -1
        ans = 1
        l = 0
        r = L - 1
        while l < r:
            if A[l] + A[r] < K:
                ans = max(A[l] + A[r], ans)
                l += 1
            else:
                r -= 1
        return -1 if ans == 1 else ans


# nums, target
IN = [([34, 23, 1, 24, 75, 33, 54, 8], 60), ([10, 20, 30], 15), ([3, 2, 4], 6)]
useSet = 0
print(Solution().twoSumLessThanK(IN[useSet][0], IN[useSet][1]))
