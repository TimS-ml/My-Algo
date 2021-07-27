# https://leetcode-cn.com/problems/single-number/


class Solution:
    def singleNumber(self, nums):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key


nums1 = [2, 2, 3]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1, 2]
print(Solution().singleNumber(nums3))
