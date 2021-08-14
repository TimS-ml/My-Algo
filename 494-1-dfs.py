'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''

from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(curr_target, idx):
            if idx == len(nums):
                return 1 if target == 0 else 0
            ans = 0
            ans += dfs(curr_target - nums[idx], idx + 1)
            ans += dfs(curr_target + nums[idx], idx + 1)
            return ans

        return dfs(target, 0)
