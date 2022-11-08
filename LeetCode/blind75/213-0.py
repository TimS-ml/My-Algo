'''
figure out max of
rob1 [1, ... n-1]
rob2  [2, ... n]
'''


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # sol of 198
        def helper(nums):
            # bottom up
            # max $ from house 1 to i max(rob i vs not rob i)
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]

            for i in range(2, len(nums) + 1):
                dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

            return dp[-1]
        
        return max(helper(nums[1:]), helper(nums[:-1]))
