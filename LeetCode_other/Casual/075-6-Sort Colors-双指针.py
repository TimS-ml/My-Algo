# https://leetcode-cn.com/problems/sort-colors/
# 左边交换完, nums[curr]的的值是0。一定要往后挪一位继续扫描。
# 而右边交换完，nums[curr]是之前的nums[p2]的值，这个值是没有被扫描过的，所以不用挪一位，直接扫描curr。


class Solution(object):
    def sortColors(self, nums):
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:  # nums[curr] == 1
                curr += 1


nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [0, 1, 2]
Solution().sortColors(nums2)
print(nums2)
