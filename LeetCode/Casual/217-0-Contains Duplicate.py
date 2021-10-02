# https://leetcode-cn.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums) -> bool:
        # for i in range(len(nums)):
        #     if nums.index(nums[i]) != i:
        #         return True
        # return False

        if len(nums) == 0 or len(nums) == 1:
            return False

        for i in range(len(nums) - 1, 0, -1):
            if nums.index(nums[i]) != i:
                return True
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums))
