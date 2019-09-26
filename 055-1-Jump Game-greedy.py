# https://leetcode-cn.com/problems/jump-game/
# 从前往后跳


class Solution:
    def canJump(self, nums) -> bool:
        start = 0
        end = 0
        while start <= end and end < len(nums)-1:
            end = max(end, nums[start]+start)
            start += 1
        return end >= len(nums)-1


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [2, 4, 2, 1, 0, 2, 0]
print(Solution().canJump(nums3))
