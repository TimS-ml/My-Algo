'''
- kws: consecutive
- brute force or dp

dp[i]:
number of arithmetic subarrays of nums[:i]

state transfer:
dp[i] = dp[i-1]

init:
dp[0~1] = 0
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        L = len(nums)
        if L < 3:
            return 0
        ans = 0
        dp = 0
        for i in range(2, L):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                ans += dp
            else:
                dp = 0
        return ans
