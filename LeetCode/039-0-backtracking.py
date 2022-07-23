'''
# Code Explain:
- Time complexity: O(N * 2^N)
    - The real complexity is lower than this
    - or O(S), where S is the sum of the lengths of all feasible solutions
- Space complexity: O(N)

For the case [1, 2, 3, 4], k = 2
after [1, 2] (len = k)
need to pop 2, then visit [1, 3]

    [1] a simple base case(s) for recursion, not a terminating senario
    - append
    [2] a set of rules for backtrack ()
    - Terminate scenario: sum(curr) == k
    - Backtrack senario: sum(curr) < k
    [3] loop over remaining pieces, need a pointer to track the position

'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(start, subset):
            if sum(subset) == target:
                ans.append(subset[:])
                return
            if sum(subset) > target:
                return
            for i in range(start, len(candidates)):
                subset.append(candidates[i])
                # print(subset)
                backtrack(i, subset)  # not i+1
                subset.pop()

        ans = []
        backtrack(0, [])
        return ans

    # avoid using sum, it will be faster
    def combinationSum_2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(start, subset, remain):
            for i in range(start, len(candidates)):
                if candidates[i] == remain:
                    ans.append(subset + [candidates[i]])
                    return
                elif candidates[i] > remain:
                    return
                else:
                    backtrack(i, subset + [candidates[i]],
                              remain - candidates[i])  # not i+1

        ans = []
        backtrack(0, [], target)
        return ans


# inputs
c = [2, 3, 6, 7]
t = 7
print(Solution().combinationSum_2(c, t))
