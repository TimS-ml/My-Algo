'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Solution
- Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
- Find the largest index l > k such that nums[k] < nums[l].
- Swap nums[k] and nums[l].
- Reverse the sub-array nums[k + 1:].

# Detail
a = [2, 5, 4, 3, 1]
     |  |     |
    idx_desc-1 idx_desc     i

- find a[idx_desc] > a[idx_desc-1] *from right*
    - 2, 5
- replace a[idx_desc-1] with number just larger than itself among the numbers lying to its right
    - swap 2, 3 
    - now we have correct number at idx_desc-1
        [3, 5, 4, 2, 1]
- reverse the numbers following a[idx_desc-1]
    - [3, 1, 2, 4, 5]

# Notation:
remember to sort !!!
lc 46: no duplication version
'''

from typing import List
import bisect


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx_desc = i = len(nums) - 1
        while idx_desc > 0 and nums[idx_desc - 1] >= nums[idx_desc]:
            idx_desc -= 1
        if idx_desc == 0:  # nums are in descending order
            nums.reverse()
            return

        idx_desc = idx_desc - 1  # find the last "ascending" position
        while nums[i] <= nums[idx_desc]:
            i -= 1

        nums[idx_desc], nums[i] = nums[i], nums[idx_desc]
        l, r = idx_desc + 1, len(nums) - 1  # reverse the second part

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

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
