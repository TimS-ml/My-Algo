# https://leetcode-cn.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 分别调整到合并, m, n的数组的最后一位序号
        end = m + n - 1
        m -= 1
        n -= 1

        # 逐个比较大小
        while end >= 0 and m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end] = nums2[n]
                n -= 1
            end -= 1

        # 特殊情况
        while n >= 0:
            nums1[end] = nums2[n]
            end -= 1
            n -= 1
        print(nums1)


# [1]
nums1 = [0]
m = 0
nums2 = [1]
n = 1

# # [1, 2, 2, 3, 5, 6]
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

Solution().merge(nums1, m, nums2, n)
