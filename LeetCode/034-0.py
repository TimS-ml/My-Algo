'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target):
            n = len(nums) - 1
            left = 0
            right = n
            while (left <= right):
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
            return left

        a = binarySearch(nums, target)
        b = binarySearch(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]
