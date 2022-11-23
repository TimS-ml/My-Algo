'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Solution

case
idx    0  1  2  3  4
in  = [2, 5, 4, 3, 1]
out = [3, 1, 2, 4, 5]

- Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
    - (the peak with least weightage), k = 0
- Find the largest index l > k such that nums[k] < nums[l].
    - l = 3
- Swap nums[k] and nums[l]
    - [3, 5, 4, 2, 1]
- Reverse the sub-array nums[k + 1:]
    - reverse 5~1, the goal is to make it in ASC order
    - [3, 1, 2, 4, 5]


# Notation:
Special case: Desc order => reverse
lc 46: no duplication version
'''

from typing import List
import bisect


class Solution:
    def nextPermutation(self, nums):
        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # nums are in descending order
        if i == 0:
            nums.reverse()
            return

        # find the last "ascending" position
        k = i - 1
        j = len(nums)-1
        while nums[j] <= nums[k]:
            j -= 1

        # swap
        nums[k], nums[j] = nums[j], nums[k]

        # reverse the second part
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

    # not recommand
    def nextPermutation_2(self, nums: List[int]) -> None:
        idx_desc = len(nums) - 1
        while idx_desc > 0:
            if nums[idx_desc] > nums[idx_desc - 1]:
                break
            idx_desc -= 1

        if idx_desc > 0:
            nums[idx_desc:] = sorted(nums[idx_desc:])
            swap_idx = bisect.bisect(nums, nums[idx_desc - 1], lo=idx_desc)
            nums[swap_idx], nums[idx_desc - 1] = nums[idx_desc - 1], nums[swap_idx]
        else:
            nums.reverse()


nums = [1, 1, 2]
print(Solution().nextPermutation(nums))
