# https://leetcode-cn.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


nums = [1, 2, 2, 3, 4]
print(Solution().findDuplicate(nums))
