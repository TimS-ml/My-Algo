'''
# Code Explain:
Init
- Time complexity: O(N)
- Space complexity: O(N)

Query
- Time complexity: O(1)
- Space complexity: O(N)

dp or preSum

nums   idx    0, 1, 2, 3, 4
preSum idx 0, 1, 2, 3, 4, 5
'''


class NumArray(object):
    def __init__(self, nums: list[int]):
        # cumsum
        self.dp = [0] * (len(nums) + 1)  # len + 1, start with 0
        for i in range(len(nums)):
            self.dp[i + 1] = self.dp[i] + nums[i]  # dp[1]=dp[0]+nums[0]

    def sumRange(self, left: int, right: int) -> int:
        # sum(nums[:right+1]) - sum(nums[:left]) = sum from left to right (include right)
        return self.dp[right + 1] - self.dp[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,right)
nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2)  # -> 1
# sumRange(2, 5)  # -> -1
# sumRange(0, 5)  # -> -3
print(NumArray(nums).sumRange(2, 5))
