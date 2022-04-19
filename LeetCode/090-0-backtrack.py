'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Same like lc 78

Pay attention on the case like [4,4,4,1,4] => sort at first
'''

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            if subset not in ans:
                ans.append(subset)
            for i in range(start, len(nums)):
                backtrack(i + 1, subset + [nums[i]])

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans

    # right way to remove duplicate
    def subsetsWithDup_2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            ans.append(subset)
            for i in range(start, len(nums)):
                # skip dupl elements
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, subset + [nums[i]])

        nums.sort()
        ans = []
        backtrack(0, [])
        return ans

    # cascade
    def subsets_3(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

# inputs
IN = [(38), (128)]
useSet = 1
print(Solution().subsetsWithDup(IN[useSet]))