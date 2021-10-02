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


# nums, target
# IN = ([11, 2, 15, 7], 19)
# IN = ([2, 7, 11, 15], 9)
IN = ([3, 2, 4], 6)
print(Solution().twoSum_2(IN[0], IN[1]))
