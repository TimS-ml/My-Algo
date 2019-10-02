# https://leetcode-cn.com/problems/wiggle-subsequence/


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) == 0:
            return 0

        up = down = 1
        for i in range(len(nums)-1):
            if nums[i]-nums[i+1] > 0:
                up = down + 1
            elif nums[i]-nums[i+1] < 0:
                down = up + 1
        return max(up, down)


nums1 = [1, 7, 4, 9, 2, 5]
nums2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(Solution().wiggleMaxLength(nums2))
