# https://leetcode-cn.com/problems/move-zeroes/
# this not gonna work if I want to move non-0 to the end


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # return nums.sort(key = lambda x: 1 if x == 0 else 0)
        return nums.sort(key=bool, reverse=True)


# nums = [0, 1, 0, 3, 12]
nums = [0, 0, 1]
print(Solution().moveZeroes(nums))
