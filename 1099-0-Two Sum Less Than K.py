# https://leetcode-cn.com/problems/two-sum-less-than-k/

from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        L = len(A)
        if not A or L < 2:
            return -1

        ans = 1
        for i in range(L):
            for j in range(i+1, L):
                if A[i] + A[j] < K:
                   ans = max(A[i] + A[j], ans) 
        return -1 if ans == 1 else ans


# nums, target
IN = [([34, 23, 1, 24, 75, 33, 54, 8], 60), ([10, 20, 30], 15), ([3, 2, 4], 6)]
useSet = 0
print(Solution().twoSumLessThanK(IN[useSet][0], IN[useSet][1]))

