'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

import pytest
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

    # solution 4 in stack + looping
    def twoSum_5(self, nums: List[int], target: int) -> List[int]:
        from collections import deque
        cache = {}
        stack = deque([0])  # a stack of idx

        while stack:
            idx = stack.popleft()
            # print(idx, cache)
            if target - nums[idx] in cache:
                return [cache[target - nums[idx]], idx]
            else:
                cache[nums[idx]] = idx
                stack.append(idx+1)


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected", 
    [([3, 2, 4], 6, [1, 2]),
     ([2, 7, 11, 15], 9, [0, 1]),
     ([11, 2, 15, 7], 18, [0, 3])]
)

def test_func(test_input_1, test_input_2, expected):
    assert Solution().twoSum_5(test_input_1, test_input_2) == expected

# pytest.main()
