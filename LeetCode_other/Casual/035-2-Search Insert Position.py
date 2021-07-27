# https://leetcode-cn.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums, target) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)  # 考虑target > len(xxx)的情况


nums = [1, 3, 5, 6]
target = 3
print(Solution().searchInsert(nums, target))
