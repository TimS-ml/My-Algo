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
'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        candidates.sort()
        trackSum = 0

        def backtrack(start, subset):
            nonlocal trackSum
            if trackSum == target:
                ans.append(subset[:])
                # if subset not in ans:
                #     ans.append(subset[:])
                return
            if trackSum > target:
                return

            for i in range(start, len(candidates)):
                # !!!
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                trackSum += candidates[i]
                backtrack(i + 1, subset)  # lc39 is i
                subset.pop()
                trackSum -= candidates[i]

        ans = []
        backtrack(0, [])
        return ans

    # using sum(subset), it's O(N)
    # def combinationSum2(self, candidates: List[int],
    #                     target: int) -> List[List[int]]:
    #     candidates.sort()

    #     def backtrack(start, subset):
    #         if sum(subset) == target:
    #             ans.append(subset[:])
    #             # if subset not in ans:
    #             #     ans.append(subset[:])
    #             return
    #         if sum(subset) > target:
    #             return
    #         for i in range(start, len(candidates)):
    #             # !!!
    #             if i > start and candidates[i] == candidates[i - 1]:
    #                 continue
    #             subset.append(candidates[i])
    #             backtrack(i + 1, subset)  # lc39 is i
    #             subset.pop()

    #     ans = []
    #     backtrack(0, [])
    #     return ans

    # avoid using sum, same as than sol 1
    def combinationSum2_2(self, candidates: List[int],
                          target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(start, subset, remain):
            for i in range(start, len(candidates)):
                # !!!
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # directly return, avoid jumpping into new subfunc stack
                if candidates[i] == remain:
                    ans.append(subset + [candidates[i]])  # !!!
                    # if subset + [candidates[i]] not in ans:
                    #     ans.append(subset + [candidates[i]])
                    return
                elif candidates[i] > remain:
                    return

                else:
                    backtrack(i + 1, subset + [candidates[i]],
                              remain - candidates[i])  # lc39 is i

        ans = []
        backtrack(0, [], target)
        return ans


# inputs
c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
t = 27
# c = [10, 1, 2, 7, 6, 1, 5]
# t = 8
print(Solution().combinationSum2(c, t))
