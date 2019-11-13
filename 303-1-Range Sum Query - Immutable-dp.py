# https://leetcode-cn.com/problems/range-sum-query-immutable/


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            self.dp[i + 1] = self.dp[i] + nums[i]  # dp[1]=dp[0]+nums[0]
        print(self.dp)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2)  # -> 1
# sumRange(2, 5)  # -> -1
# sumRange(0, 5)  # -> -3
print(NumArray(nums).sumRange(2, 5))
