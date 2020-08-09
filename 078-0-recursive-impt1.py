'''
# Code Explain:
- Time complexity: O(N*2^N)
    N times (2 to the power of N)
    2^N: number of subsets of N elements
    For a given number, it could be present or absent (i.e. binary choice) in a subset solution
- Space complexity: O(N*2^N)

It is tricky to ensure that the generated solutions are complete and non-redundant

- Start from an empty subsets
- Take 1 into consideration and add new subsets by updating existing ones
- Take 2 into consideration xxx
    ...

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
        - update existing subsets 
    [2] a set of rules: recurrence relation
        - add new element
    [3] terminating senario
        - end of list

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            ans += [curr + [i] for curr in ans]
            # print(i, ans)
        return ans


# inputs
IN = [
    ([1, 2, 3]), 
    ([1, 2, 3, 4])
]
useSet = 1
print(Solution().subsets(IN[useSet]))

