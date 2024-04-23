'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

dp[i]: max money until rob house i

case 1
nums =  [2, 7, 9, 3, 1]
dp = [0, 2, 7, x, y, z]

x could be 2 + 9 (include current)
        or 7

y could be 7 + 3 (include current)
        or 2 + 3 (include current, skip 2)
        or 11

z could be 11 + 1 (include current)
        or 7 + 1 (include current, skip 2)
        or 11

z could not be 2 + 1 (skip 3)

you don't need to consider skip 2 either:
nums =  [99,  7, 9, 3]
dp = [0, 99, 99, x, y]

x could be 99 + 9 (include current)
        or 7

y could be 99 + 3 (include current, note: this 99 is from dp[i - 2])
        or 108

see, the dp[1] = dp[2] = 99
test case of the question hide this info
'''

from typing import List


class Solution:
    # dp[i]: max money until rob house i
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        dp = [0] * (len(nums) + 1)
        dp[1], dp[2] = nums[0], nums[1]
        for i in range(2, len(nums)):
            rob_curr = dp[i - 1] + nums[i]
            rob_curr2 = dp[i - 2] + nums[i]
            skip_curr = dp[i]
            dp[i + 1] = max([rob_curr, rob_curr2, skip_curr])

        return dp[-1]

    # dp[i]: max money until rob house i
    def rob_2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        dp = [0] * len(nums)
        # dp[0], dp[1] = nums[0], nums[1]
        # you init woring!!! should be this according to your dp definitation:
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            rob_curr = dp[i - 2] + nums[i]
            skip_curr = dp[i - 1]
            print(dp, dp[i - 2] + nums[i], dp[i - 1])
            dp[i] = max(rob_curr, skip_curr)

        return dp[-1]


nums = [2, 1, 1, 2]
print(Solution().rob_wrong(nums))
