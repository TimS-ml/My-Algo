# https://leetcode-cn.com/problems/largest-time-for-given-digits/
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from typing import List
import itertools


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
        for p in itertools.permutations(sorted(A, reverse=True)):
            if p[0] * 10 + p[1] < 24 and p[2] < 6:
                return f"{p[0]}{p[1]}:{p[2]}{p[3]}"
        return ''


A1 = [1, 2, 3, 4]
A2 = [0, 1, 2, 3]
A3 = [5, 5, 5, 5]
print(Solution().largestTimeFromDigits(A2))
