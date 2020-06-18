# https://leetcode-cn.com/problems/rotate-array/
# ok... unfinish

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1


# nums, k
IN = [([1, 2, 3, 4, 5, 6, 7], 3)]
useSet = 0
print(Solution().rotate(IN[useSet][0], IN[useSet][1]))
