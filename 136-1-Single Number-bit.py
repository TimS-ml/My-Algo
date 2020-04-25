# https://leetcode-cn.com/problems/single-number/
# https://en.wikipedia.org/wiki/XOR_gate
# Try this: it will return 0
# x = y = 2
# x ^= y

import pysnooper


@pysnooper.snoop()
class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums2))

