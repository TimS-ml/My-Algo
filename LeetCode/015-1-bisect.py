'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O()

This is way faster since it includes bisect

# Pros and Cons:
## Pros:

## Cons:

# Notation:
!!! Sort first before using bisect !!!
Dicts preserve insertion order in Python 3.7+
'''

from typing import List
from bisect import bisect_left, bisect_right  # binary search
import collections


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        if length < 3:
            return ans

        # remove duplicate of nums
        # dic = {}
        # for i in range(len(nums)):
        #     dic[nums[i]] = dic.get(nums[i], 0) + 1
        # nums = sorted(dic)
        dic = collections.Counter(nums)
        nums = sorted(dic)
        print(dic, nums)

        ans = []
        for i, v in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if v == 0:
                if dic[v] > 2:
                    ans.append([0, 0, 0])
            # case ii. two numbers are the same
            elif dic[v] > 1 and -2 * v in dic:
                ans.append([v, v, -2 * v])
            # case iii. not any of the three numbers are the same
            if v < 0:
                target = 0 - v
                left = bisect_left(nums, target - nums[-1], i + 1)
                right = bisect_right(nums, target / 2, left)
                for a in nums[left:right]:
                    b = target - a
                    if b in dic and a != b:
                        ans.append([v, a, b])
        return ans


# inputs
nums = [-1, 0, 1, 2, -1, -4]
# nums = [-2, 0, 1, 1, 2]
# nums = [-1, 0, 0, 0, 1, 1]
print(Solution().threeSum(nums))
