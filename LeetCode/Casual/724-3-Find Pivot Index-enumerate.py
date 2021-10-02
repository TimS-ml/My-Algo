# https://leetcode-cn.com/problems/find-pivot-index/
# sum [0,i-1] == sum [i+1,-1] <=> 2*sum [0,i-1] == sum(nums)-nums[i]
# modified version of version 1
# Link about liter speed
# https://blog.csdn.net/weixin_38243861/article/details/81701534

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        SUM = sum(nums)
        L = 0
        for k, v in enumerate(nums):
            if 2 * L == SUM - v:
                return k
            L += v
        return -1


nums = [1, 7, 3, 6, 5, 6]
nums2 = [1, -1, -1, 0, 1, -9]
print(Solution().pivotIndex(nums2))
