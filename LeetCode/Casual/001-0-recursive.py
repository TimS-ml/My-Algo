'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    # really slow solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                return [i, nums.index(target - nums[i])]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for key, value in enumerate(nums):
            if value in d:
                return [d[value], key]
            d[target - value] = key

    # same as sol 2
    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i
    
    # recursion: reverse for loop of solution 3
    def twoSum_4(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        def helper(idx):
            # print(idx, cache)
            if target - nums[idx] in cache:
                return [cache[target - nums[idx]], idx]
            else:
                cache[nums[idx]] = idx
                return helper(idx+1)

        return helper(0)

# nums, target
# IN = ([11, 2, 15, 7], 19)
# IN = ([2, 7, 11, 15], 9)
IN = ([3, 2, 4], 6)
print(Solution().twoSum_4(IN[0], IN[1]))
