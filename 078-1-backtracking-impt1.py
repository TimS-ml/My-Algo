'''
# Code Explain:
- Time complexity: O(N*2^N)
- Space complexity: O(N*2^N)

Power set is all possible combinations of all possible lengths, from 0 to n

Backtracking is an algorithm for finding all solutions by exploring all potential candidates
If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again

In a backtracking, we need:
    [1] a simple base case(s) for recursion, not a terminating senario
    [2] a set of rules for backtrack ()
    [3] loop over remaining pieces, need a pointer to track the position

# Pros and Cons:
## Pros:

## Cons:

# Notation:
The solution include empty list
'''

from typing import List


class Solution:
    # This is not a good example:
    # loop outside backtrack
    # `k` is unnecessary
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

    def subsets2(self, nums):
        def backtrack(start, subset):
            ans.append(subset[:])
            for i in range(start, len(nums)):
                backtrack(i + 1, subset + [nums[i]])
                print('After:', subset)

        ans = []
        backtrack(0, [])
        return ans


# inputs
IN = [([1, 2, 3]), ([1, 2, 3, 4])]
useSet = 0
print(Solution().subsets(IN[useSet]))
