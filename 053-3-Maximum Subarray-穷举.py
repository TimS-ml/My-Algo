# https://leetcode-cn.com/problems/maximum-subarray/
# 但是超时了……


class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                value = 0
                for k in range(i, j + 1):
                    value += nums[k]
                maxSum = max(value, maxSum)
        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-2, 1]
print(Solution().maxSubArray(nums))
