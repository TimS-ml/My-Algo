# https://leetcode-cn.com/problems/rotate-array/


class Solution:
    def rotate(nums, k):
        if len(nums) == 0 or k == 0:
            return

        # start和end对应要交换的数组的序号，最终实现部分翻转
        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        n = len(nums) - 1 # 末尾元素的序号
        k = k % len(nums) # 如果k比len(nums)大，就跳过重复循环
        # [4, 3, 2, 1, 5, 6, 7]
        # [4, 3, 2, 1, 7, 6, 5]
        # [5, 6, 7, 1, 2, 3, 4]
        reverse(0, n - k, nums) # 翻转前面
        reverse(n - k + 1, n, nums) # 翻转后面
        reverse(0, n, nums) # 全翻转
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution.rotate(nums, k)
