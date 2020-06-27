# https://leetcode-cn.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums, target) -> int:
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)


nums = [1, 3, 5, 6]
target = 4
print(Solution().searchInsert(nums, target))
