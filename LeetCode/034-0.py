'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

what if nums not in target???
'''

from typing import List


class Solution:
    # [left, right)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        ans = []

        # left bond
        left, right = 0, len(nums)
        key = -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                key = mid
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        # if left == len(nums) or nums[left] != target:
        #     return [-1, -1]
        if key == -1:
            return [-1, -1]
        ans.append(left)

        # right bond
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        ans.append(left - 1)
        
        return ans

    # not recommended...
    def searchRange_2(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            while (left <= right):
                mid = left + (left - right) // 2
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
