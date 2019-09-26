# https://leetcode-cn.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        return int((n * (n + 1)) / 2 - sum(nums))