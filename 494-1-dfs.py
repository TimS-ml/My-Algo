'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/

dp: 
- 第一位是目前的和, 第二位是目前的位数, 值是这个元祖推导到最后能有多少个解
- 深入到最后一位时, 再深入就超了位数限制了, 此时可以直接判断这个节点的和是否等于需要的S

'''

from typing import List
# from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(cur_sum, i, cache):
            if i < len(nums) and (cur_sum, i) not in cache:  # 搜索周围节点
                cache[(cur_sum, i)] = dfs(cur_sum + nums[i], i + 1, cache) + \
                                      dfs(cur_sum - nums[i], i + 1, cache)
            # if last digit (i == len(nums), no i+1 anymore), check sum directly
            return cache.get((cur_sum, i), int(cur_sum == target))

        return dfs(0, 0, cache)
