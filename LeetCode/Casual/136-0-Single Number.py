# https://leetcode-cn.com/problems/single-number/


class Solution:
    def singleNumber(self, nums):
        # for i in range(len(nums)):
        #     indexlist = [index for index, value in enumerate(nums) if value == nums[i]]
        #     if len(indexlist) == 1:
        #         return nums[i]
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1] and nums[i] != nums[i - 1]:
                return nums[i]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]


nums1 = [2, 2, 3]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1, 2]
print(Solution().singleNumber(nums3))
