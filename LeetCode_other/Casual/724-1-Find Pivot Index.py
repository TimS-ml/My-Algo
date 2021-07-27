# https://leetcode-cn.com/problems/find-pivot-index/
# sum [0,i-1] == sum [i+1,-1] <=> 2*sum [0,i-1] == sum(nums)-nums[i]
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if sum(nums[1:]) == 0:
            return 0
        L, SUM = nums[0], sum(nums)
        for i in range(1, len(nums)):
            if 2 * L == SUM - nums[i]:
                return i
            L += nums[i]
        return -1


nums = [1, 7, 3, 6, 5, 6]
nums2 = [1, -1, -1, 0, 1, -9]
print(Solution().pivotIndex(nums2))
