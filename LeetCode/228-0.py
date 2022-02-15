'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)


- we need 2 pointers
  - low and high
  - if low == high:
    - single element
  - else:
    - low -> high
'''
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # add a number at end of list to avoid out of range
        nums.append(2**32)
        ans, start = [], 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if i - 1 == start:
                    ans.append(str(nums[start]))
                else:
                    ans.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        return ans


nums = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges(nums))
