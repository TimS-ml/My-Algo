'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

https://en.wikipedia.org/wiki/XOR_gate
Try this: it will return 0
x = y = 2
x ^= y

Or you can directly return
return 2 * sum(set(nums)) - sum(nums)
'''

from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


    def singleNumber_2(self, nums):
        # return reduce(lambda x, y: x ^ y, nums)
        return reduce(operator.xor, nums)


nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums2))
