'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    def searchInsert(self, nums, target) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left


nums = [1, 3, 5, 6]
target = 2
print(Solution().searchInsert(nums, target))
