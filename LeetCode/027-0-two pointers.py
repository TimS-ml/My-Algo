'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow

    # def removeElement_2(self, nums: List[int], val: int) -> int:
    #     while val in nums:
    #         nums.remove(val)
    #     return len(nums)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
