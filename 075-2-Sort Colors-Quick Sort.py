# https://leetcode-cn.com/problems/sort-colors/
# http://jalan.space/leetcode-notebook/#/algorithm/sort/quick/?id=_75-sort-colors


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums)-1)
        #print nums

    def quickSort(self, nums, left, right):
        if left > right:
            return
        i = left
        j = right
        tmp = nums[i]
        while i != j:
            while nums[j] >= tmp and j > i:
                j = j - 1
            while nums[i] <= tmp and i < j:
                i = i + 1
            if i < j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
        # 交换基准数
        nums[left] = nums[i]
        nums[i] = tmp
        self.quickSort(nums, left, i-1)
        self.quickSort(nums, i+1, right)


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
