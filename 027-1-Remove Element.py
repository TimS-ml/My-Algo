# https://leetcode-cn.com/problems/remove-element/
# 没有改变数组，挺巧的


class Solution:
    def removeElement(self, nums, val) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
        return len(nums) - count


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
