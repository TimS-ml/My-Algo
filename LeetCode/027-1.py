'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

You can customize the sort function, to replace 'move'
And simply calculate and return the correct position
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        position = len(nums) - nums.count(val)
        nums.sort(key=lambda x: x != val, reverse=True)
        return position


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
