# https://leetcode-cn.com/problems/move-zeroes/
# do [len(nums) - number of 0] times operation


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_in = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums.insert(num_in, nums.pop(i))
                num_in += 1
        return nums


# nums = [0, 1, 0, 3, 12]
nums = [0, 0, 1]
print(Solution().moveZeroes(nums))
