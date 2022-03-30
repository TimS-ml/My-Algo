'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

List del: O(N), so if we delete val, time: O(N^2)
'''

from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        # fast and slow
        i = 1
        j = 0
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1


# n = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n = [1, 1, 2]
# n = []

print(Solution().removeDuplicates(n))
