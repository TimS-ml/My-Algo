# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0 or L == 1:
            return L

        i = 1
        j = 0
        while i < len(nums):
            qick = nums[i]
            slow = nums[j]
            if qick == slow:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
        return j + 1


IN = [([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), ([1, 1, 2]), ([])]
useSet = 2
print(Solution().removeDuplicates(IN[useSet]))
