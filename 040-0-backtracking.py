'''
# Code Explain:
- Time complexity: O(2^N * N)
- Space complexity: O(N)

    [1] a simple base case(s) for recursion, not a terminating senario
    - append
    [2] a set of rules for backtrack ()
    - Terminate scenario: sum(curr) == k
    - Backtrack senario: sum(curr) < k
    [3] loop over remaining pieces, need a pointer to track the position

for sol 3:
if c = [1, 1, 1, 3], target = 3
the subset [1, 1, 1] comes from i == start

# Pros and Cons:
## Pros:

## Cons:

# Notation:
unlike LC039, this question requires elements only occur once

shallow copy:
    subset[:]
'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(start, subset):
            if sum(subset) == target:
                if subset not in ans:
                    ans.append(subset[:])
                return
            if sum(subset) > target:
                return
            for i in range(start, len(candidates)):
                subset.append(candidates[i])
                # print(subset)
                backtrack(i+1, subset)
                subset.pop()

        ans = []
        backtrack(0, [])
        return ans

    # avoid using sum, it will be faster
    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(start, subset, remain):
            for i in range(start, len(candidates)):
                if candidates[i] == remain:
                    if subset + [candidates[i]] not in ans:
                        ans.append(subset + [candidates[i]])
                    return
                elif candidates[i] > remain:
                    return
                else:
                    backtrack(i+1, subset + [candidates[i]], remain - candidates[i])

        ans = []
        backtrack(0, [], target)
        return ans

    # avoid duplicate
    def combinationSum23(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(start, subset, remain):
            for i in range(start, len(candidates)):
                if candidates[i] == remain:
                    ans.append(subset + [candidates[i]])
                    return
                elif candidates[i] > remain:
                    return
                # skip the >2nd duplicate element
                elif i > start and candidates[i-1] == candidates[i]:
                    continue
                else:
                    backtrack(i+1, subset + [candidates[i]], remain - candidates[i])

        ans = []
        backtrack(0, [], target)
        return ans

# inputs
c = [10,1,2,7,6,1,5]
t = 8
print(Solution().combinationSum23(c, t))

