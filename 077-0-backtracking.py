'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

For the case [1, 2, 3, 4], k = 2
after [1, 2] (len = k)
need to pop 2, then visit [1, 3]

    [1] a simple base case(s) for recursion, not a terminating senario
    - append
    [2] a set of rules for backtrack ()
    - Terminate scenario: len(curr) == k
    - Backtrack senario: len(curr) < k
    [3] loop over remaining pieces, need a pointer to track the position


# Pros and Cons:
## Pros:

## Cons:

# Notation:
shallow copy:
    subset[:]
'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]

        def backtrack(start, subset):
            if len(subset) == k:
                ans.append(subset[:])
                return
            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        ans = []
        backtrack(0, [])
        return ans


# inputs
n = 4
k = 2
print(Solution().combine(n, k))
