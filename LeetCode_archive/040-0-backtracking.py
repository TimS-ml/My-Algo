'''
# Code Explain:
- Time complexity: O(2^N * N)
- Space complexity: O(N)

what 'skip dupl' do:
if c = [1, 1, 1, 1, 3], target = 5
backtrack idx=0
for i in range(idx, len)
- find c0, c1, c4
    - idx=1, t=4
    - skip start with c2 to c3
- skip start with c1 to c3
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
                return
            if trackSum > target:
                return

            for i in range(start, len(candidates)):
                # skip dupl elements
                # case: 2, 2' and 2', 2
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                trackSum += candidates[i]  # !!! trackSum and subset are tight together
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
