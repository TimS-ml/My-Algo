'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

input: [a1, a2 ... an-1, an]

brute force:
[1] rob first:
in:    [a1, a2 ... an-1]

[2] skip first:
in:         [a2 ... an-1, an]
'''

class Solution:
    # brute force
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        def rob_house(nums):
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]

            for i in range(2, len(nums) + 1):
                print(dp, dp[i-2] + nums[i-1], dp[i-1])
                dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

            return dp[-1]

        ans = max(rob_house(nums[1:]), rob_house(nums[:-1]))
        return ans

