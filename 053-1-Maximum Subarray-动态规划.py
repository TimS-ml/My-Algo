# https://leetcode-cn.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])  # 这样有利于找到前n个数里sum最大的
            maxSum = max(maxSum, preSum)
        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
