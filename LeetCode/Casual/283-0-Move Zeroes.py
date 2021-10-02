# https://leetcode-cn.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        place = []
        for k, v in enumerate(nums):
            if v == 0:
                place.append(k)
        while place:
            p = place.pop()
            nums.append(nums.pop(p))
        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
