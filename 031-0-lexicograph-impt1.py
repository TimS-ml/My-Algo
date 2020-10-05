'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

a = [2, 5, 4, 3, 1]
     |  |     |
    i-1 i     j

- find a[i] > a[i-1] *from right*
    - 2, 5
- replace a[i-1] with number just larger than itself among the numbers lying to its right
    - swap 2, 3 
    - now we have correct number at i-1
        [3, 5, 4, 2, 1]
- reverse the numbers following a[i-1]
    - [3, 1, 2, 4, 5]

# Pros and Cons:
## Pros:

## Cons:

# Notation:
remember to sort !!!
LC046: no duplication version
'''

from typing import List
import bisect


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:  # nums are in descending order
            nums.reverse()
            return
        k = i - 1  # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def nextPermutation2(self, nums: List[int]) -> None:
        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                break
            index -= 1

        if index > 0:
            nums[index:] = sorted(nums[index:])
            swap_index = bisect.bisect(nums, nums[index - 1], lo=index)
            nums[swap_index], nums[index - 1] = nums[index -
                                                     1], nums[swap_index]
        else:
            nums.reverse()


nums = [1, 1, 2]
print(Solution().nextPermutation(nums))
