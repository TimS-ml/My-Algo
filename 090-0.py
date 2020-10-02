'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Same like lc 78

# Pros and Cons:
## Pros:

## Cons:

# Notation:
Pay attention on the case like [4,4,4,1,4]
'''

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            print('Before:', subset)
            if subset not in ans:
                ans.append(subset)
            for i in range(start, len(nums)):
                backtrack(i + 1, subset + [nums[i]])
                print('After:', subset)

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack2(start, subset):
            ans.append(subset)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack2(i + 1, subset + [nums[i]])

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans


# inputs
IN = [(38), (128)]
useSet = 1
print(Solution().subsetsWithDup(IN[useSet]))
