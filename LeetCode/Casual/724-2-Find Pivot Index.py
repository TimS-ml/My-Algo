# https://leetcode-cn.com/problems/find-pivot-index/
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if sum(nums[1:]) == 0:
            return 0
        L, R = nums[0], sum(nums[2:])
        for i in range(1, len(nums) - 1):
            if L == R:
                return i
            L += nums[i]
            R -= nums[i + 1]
        if sum(nums[:-1]) == 0:
            return len(nums) - 1
        return -1


nums = [1, 7, 3, 6, 5, 6]
nums2 = [1, -1, -1, 0, 1, -9]
print(Solution().pivotIndex(nums2))
