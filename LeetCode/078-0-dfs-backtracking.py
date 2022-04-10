'''
# Code Explain:
- Time complexity: O(N*2^N)
    N times (2 to the power of N)
    2^N: number of subsets of N elements
    For a given number, it could be present or absent (i.e. binary choice) in a subset solution
- Space complexity: O(N*2^N)

It is tricky to ensure that the generated solutions are complete and non-redundant

'''

from typing import List


class Solution:
    def subsets(self, nums):
        def backtrack(start, subset):
            ans.append(subset[:])
            for i in range(start, len(nums)):
                backtrack(i + 1, subset + [nums[i]])

        ans = []
        backtrack(0, [])
        return ans

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            # subset[:] create a shallow copy of the list
            if len(subset) == k:
                ans.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                # print('After:', subset)
                subset.pop()
                # print(subset.pop())

        ans = []
        for k in range(len(nums) + 1):
            backtrack(0, [])
        return ans

    def subsets_3(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            ans += [curr + [i] for curr in ans]
            # print(i, ans)
        return ans


# inputs
IN = [([1, 2, 3]), ([1, 2, 3, 4])]
useSet = 1
print(Solution().subsets(IN[useSet]))
