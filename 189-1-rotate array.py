# https://leetcode-cn.com/problems/rotate-array/


class Solution:
    def rotate(nums, k):
        if len(nums) == 0 or k == 0:
            return

        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        n = len(nums) - 1
        k = k % len(nums)  # in case k > len(nums)
        # [4, 3, 2, 1, 5, 6, 7]
        reverse(0, n - k, nums)
        # [4, 3, 2, 1, 7, 6, 5]
        reverse(n - k + 1, n, nums)
        # [5, 6, 7, 1, 2, 3, 4]
        reverse(0, n, nums)
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution.rotate(nums, k)
