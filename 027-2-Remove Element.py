# https://leetcode-cn.com/problems/remove-element/
# 改变数组的前几项，数组长度没变


class Solution:
    def removeElement(self, nums, val) -> int:
        slow = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                slow += 1
                nums[slow] = nums[i]
        print(nums)
        return slow + 1


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
