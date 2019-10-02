# https://leetcode-cn.com/problems/rotate-array/
# 逐个向左移动


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0:
            return

        end = len(nums) - 1
        k = k % len(nums)  # 如果k比len(nums)大，就跳过重复循环

        for i in range(0, k):
            temp = nums[end]
            for j in range(0, end):
                nums[j] = nums[j - 1]
            nums[0] = temp


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
