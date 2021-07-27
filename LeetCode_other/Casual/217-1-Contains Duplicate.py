# https://leetcode-cn.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False

        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums))
