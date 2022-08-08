'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O()

'''

from typing import List


class Solution:
    # [left, right]
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

    # [left, right), mainly modify r side
    def search_2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            # update pivot every time
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot  # note: since l < r
            else:
                left = pivot + 1

        return -1

