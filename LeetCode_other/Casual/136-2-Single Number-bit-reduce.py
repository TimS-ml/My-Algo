# https://leetcode-cn.com/problems/single-number/
# https://www.geeksforgeeks.org/reduce-in-python/
# reduce only return a single number accumulated
# so this not gonna work if return 2 or more numbers

import functiontools


class Solution:
    def singleNumber(self, nums):
        # return reduce(lambda x, y: x ^ y, nums)
        return reduce(operator.xor, nums)


nums1 = [2, 2, 3]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1, 2]
print(Solution().singleNumber(nums3))
