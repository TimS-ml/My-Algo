# https://leetcode-cn.com/problems/sort-colors/
# http://jalan.space/leetcode-notebook/#/algorithm/sort/quick/?id=_75-sort-colors
# str.index(str, beg=0, end=len(string))


class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums) - 1):  # i是有序区和无序区的分界
            if nums[i] > min(nums[i:]):
                min_index = nums.index(min(nums[i:]), i)
                nums[i], nums[min_index] = nums[min_index], nums[i]
        print(nums)


nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [0, 1, 2]
Solution().sortColors(nums2)
print(nums2)
