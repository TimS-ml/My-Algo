'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O()

'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:  # note: <=, since r start with len-1
            # update pivot every time
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:  # if you do this way
            # update pivot every time
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        if nums[left] == target:
            return left
        else:
            return -1

