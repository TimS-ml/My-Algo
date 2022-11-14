class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        dp = [1] * (len(nums) + 1)
        
        for i in range(2, len(dp)):
            for j in range(1, i):
                if nums[j-1] < nums[i-1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)
        
