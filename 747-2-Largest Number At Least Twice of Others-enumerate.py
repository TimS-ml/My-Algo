# https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        m = -1
        m2 = -1
        mIndex = 0

        for i, n in enumerate(nums):
            if n >= m:
                m2 = m
                m = n
                mIndex = i
            elif n > m2:
                m2 = n

        if m < m2*2:
            mIndex = -1

        return mIndex


nums = [3, 6, 1, 0]
print(Solution().dominantIndex(nums))
