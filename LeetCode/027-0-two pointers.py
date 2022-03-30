'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''
from typing import List

class Solution:
    # fast slow pointers
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow

    # this is super slow
    # def removeElement_x(self, nums: List[int], val: int) -> int:
    #     while val in nums:
    #         nums.remove(val)
    #     return len(nums)


    # You can customize the sort function, to replace 'move'
    # And simply calculate and return the correct position
    def removeElement_2(self, nums: List[int], val: int) -> int:
        position = len(nums) - nums.count(val)
        nums.sort(key=lambda x: x != val, reverse=True)
        return position

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
