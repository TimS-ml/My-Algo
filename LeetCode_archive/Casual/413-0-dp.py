'''
- kws: consecutive
- brute force or dp
- arithmetic slices:
    max len = n
    nums(len window = n) + nums(len window = n-1) ... nums(len window = 3)
    1 + 2 + 3 ... n-2
    (n-2+1) * (n-2)/2 = (n-1)(n-2)/2

- [1] get the number and length of arithmetic subarrays block
- [2] result = ...

dp[i]:
number of arithmetic subarrays of nums[:i]

state transfer:
if difference between any two consecutive elements is the same:
    dp[i] = dp[i-1] + (n-2)
    we need to know where the seq start

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
