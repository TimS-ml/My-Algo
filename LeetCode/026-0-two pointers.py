from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 1
        j = 0
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1


IN = [([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), ([1, 1, 2]), ([])]
useSet = 2
print(Solution().removeDuplicates(IN[useSet]))
