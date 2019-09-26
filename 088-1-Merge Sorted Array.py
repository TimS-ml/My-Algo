# https://leetcode-cn.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0, n):
            nums1[i+m] = nums2[i]
        nums1.sort()
        print(nums1)


# [1, 2, 2, 3, 5, 6]
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Solution().merge(nums1, m, nums2, n)
