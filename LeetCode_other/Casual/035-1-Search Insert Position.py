# https://leetcode-cn.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums, target) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = int(lo + (hi - lo) / 2)
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return lo


nums = [1, 3, 5, 6]
target = 2
print(Solution().searchInsert(nums, target))
