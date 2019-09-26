# https://leetcode-cn.com/problems/sort-colors/
# http://jalan.space/leetcode-notebook/#/algorithm/sort/quick/?id=_75-sort-colors


class Solution(object):
    def sortColors(self, nums):
        self.popSort(nums)

    def popSort(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            for index in range(0, j):
                a = nums[index]
                b = nums[index + 1]
                if a > b:
                    nums[index + 1] = a
                    nums[index] = b
            j -= 1
        return nums


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
