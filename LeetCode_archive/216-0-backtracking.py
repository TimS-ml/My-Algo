'''
# Code Explain:
- Time complexity: O(2^N * N)
- Space complexity: O(N)

for the case k, n = 3, 7
    [1] a simple base case(s) for recursion, not a terminating senario
    - append
    [2] a set of rules for backtrack ()
    - Terminate scenario:
        - len(curr) == k  (1, 2, 3)
        - sum(curr) > n  (4, 5)
    - Backtrack senario: samilarly
    [3] loop over remaining pieces, need a pointer to track the position

for sol 3:
if c = [1, 1, 1, 3], n = 3
the subset [1, 1, 1] comes from i == start

'''

from typing import List


class Solution:
    # avoid using sum, it will be faster
    # avoid duplicate
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i + 1 for i in range(9)]
        trackSum = 0

        def backtrack(start, subset):
            nonlocal trackSum
            if trackSum == n and len(subset) == k:
                ans.append(subset[:])
                return
            if trackSum > n or len(subset) == k + 1:
                return

            for i in range(start, len(nums)):
                subset.append(nums[i])
                trackSum += nums[i]
                backtrack(i + 1, subset)
                subset.pop()
                trackSum -= nums[i]

        ans = []
        backtrack(0, [])
        return ans

    def combinationSum3_2(self, k: int, n: int) -> List[List[int]]:
        nums = [i + 1 for i in range(9)]

        def backtrack(start, subset, remain):
            for i in range(start, len(nums)):
                if nums[i] == remain and len(subset) == k - 1:
                    ans.append(subset + [nums[i]])
                    return
                elif nums[i] > remain or len(subset) == k:
                    return
                else:
                    backtrack(i + 1, subset + [nums[i]],
                              remain - nums[i])  # i+1: only appear once

        ans = []
        backtrack(0, [], n)
        return ans


# [[1, 2, 4]]
k = 3
n = 7
print(Solution().combinationSum3(k, n))
