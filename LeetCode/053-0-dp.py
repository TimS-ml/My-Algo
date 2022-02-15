'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''


class Solution(object):
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [float('-inf') for _ in range(len(nums))]

        dp[0] = nums[0]
        res = nums[0]
        for each in range(1, len(nums)):
            dp[each] = max(dp[each - 1] + nums[each], nums[each])
            res = max(res, dp[each])
            #print dp
        return res

    # rolling optimization
    def maxSubArray_2(self, nums) -> int:
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])  # 这样有利于找到前n个数里sum最大的
            maxSum = max(maxSum, preSum)
        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
