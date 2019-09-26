# https://leetcode-cn.com/problems/single-number/
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？


class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]  # 按位运算符,把数字看作二进制来进行计算
        return nums[0]


nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums2))
