'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1] * len(nums)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                ans[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans
