# https://leetcode-cn.com/problems/jump-game/
# 从后往前推, simplified version


class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        last_position = n - 1
        for i in range(n - 1, -1, -1):
            if (nums[i] + i) >= last_position:
                last_position = i
        return last_position == 0


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [2, 4, 2, 1, 0, 2, 0]
print(Solution().canJump(nums3))
