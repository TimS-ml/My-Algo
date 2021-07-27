# https://leetcode-cn.com/problems/house-robber/
# 如果偷了第i+1号屋子，收益为nums[i] + dp[i-2] (因为相邻不可偷)
# 如果不偷，收益为dp[i-1]
# 比如如果偷第4号屋子，收益为nums[3]-4号屋 + dp[1]-前2屋的收益
# 如果不偷，收益为dp[2]-前3屋的收益
# 逐步求最大值即可


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for i in range(0, 2)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            # 要么取中间的，要么取两边的
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
        return dp[(len(nums) - 1) % 2]


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
