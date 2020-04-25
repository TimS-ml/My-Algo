# https://leetcode-cn.com/problems/single-number/


class Solution:
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


nums1 = [2, 2, 3]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1, 2]
print(Solution().singleNumber(nums3))
