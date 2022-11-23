'''
case: rob
1, 3, 6, 8 ....

if rob i, then the next:
    rob i + 2 or i + 3 (i + 2 + 2 is i + 4)

two types of way to define DP
[1] dp[i] is the max value of robing house 1 to i (must rob i)
    return max(dp[-1], dp[-2])

[2] dp[i] is the max value of robing house 1 to i (until i)
    return dp[-1]
    this is better
    at i, if rob i, then its nums[i-1] (current val) + dp[i-2]
        , if not rob i, its  dp[i-1]
'''


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # bottom up
        # max $ from house 1 to i (must rob i)
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i-1]

        return max(dp[-1], dp[-2])

    # neetcode solution in dp
    def rob_mod(self, nums: List[int]) -> int:
        # bottom up
        # max $ from house 1 to i max(rob i vs not rob i)
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        return dp[-1]

    # neetcode solution
    def rob_mod_2(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob_2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        cache = {}

        # top down
        # max $ from house 1 to i (must rob i)
        def helper(i):
            # !!!
            if i == 0:
                return 0

            if i <= 2:
                return nums[i-1]

            if i in cache:
                return cache[i]

            ans = max(helper(i-2), helper(i-3)) + nums[i-1]
            cache[i] = ans
            return ans

        return max(helper(len(nums)-1), helper(len(nums)))
