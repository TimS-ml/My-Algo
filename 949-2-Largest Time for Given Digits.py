# https://leetcode-cn.com/problems/largest-time-for-given-digits/
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from typing import List
import itertools


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ''
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    if i == j or i == k or j == k:
                        continue
                    hour, minute = str(a) + str(b), str(c) + \
                        str(A[6 - i - j - k])  # sum of index: 0 + ... + 3 = 6
                    if hour < '24' and minute < '60':
                        ans = max(ans, hour + ':' + minute)
        return ans


A1 = [1, 2, 3, 4]
A2 = [0, 1, 2, 3]
A3 = [5, 5, 5, 5]
print(Solution().largestTimeFromDigits(A2))
