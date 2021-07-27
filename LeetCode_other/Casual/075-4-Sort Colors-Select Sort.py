# https://leetcode-cn.com/problems/sort-colors/
# http://jalan.space/leetcode-notebook/#/algorithm/sort/quick/?id=_75-sort-colors


class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums) - 1):  # i是有序区和无序区的分界
            min_index = i  # 最小值index
            min_num = nums[i]
            for j in range(i, len(nums)):
                if nums[j] < min_num:
                    min_num = nums[j]  # 找到最小值
                    min_index = j
            # print(nums[min_index])
            if i != min_index:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        # print(nums)


nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [0, 1, 2]
Solution().sortColors(nums2)
print(nums2)
