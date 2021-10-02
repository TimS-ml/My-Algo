# https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/
# https://www.programiz.com/python-programming/methods/built-in/all
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        # print([m >= 2*x for x in nums if x != m])
        # print([m >= 2*x for x in nums])  # False when nums.index, so will return False in all(xxx) function
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1


nums = [3, 6, 1, 0]
print(Solution().dominantIndex(nums))
