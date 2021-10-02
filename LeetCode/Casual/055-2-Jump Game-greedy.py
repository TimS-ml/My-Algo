# https://leetcode-cn.com/problems/jump-game/
# 从后往前推


class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        start = n - 2
        end = n - 1
        while start >= 0:
            if start + nums[start] >= end:
                end = start
            start -= 1
        return end <= 0


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [2, 4, 2, 1, 0, 2, 0]
print(Solution().canJump(nums3))
