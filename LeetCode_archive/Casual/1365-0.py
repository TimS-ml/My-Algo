'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)


case: [8, 1, 2, 2, 3]
- sort list [8, 1, 2, 2, 3]
- ans[i] = len(nums[k:]) k is the first number that smaller than ans[i]
'''

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        ans = []
        for i in range(len(nums)):
            ans.append(sorted_num.index(nums[i]))
        return ans


# nums = [8, 1, 2, 2, 3]
nums = [7, 7, 7, 7]
print(Solution().smallerNumbersThanCurrent(nums))
