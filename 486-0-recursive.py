'''
# Code Explain:
- Time complexity: O(2^n)
- Space complexity: O(n)

- player picks either start or end
    -> remain a continue arr
    -> use start / stop to track position
- var `turn` change from +1 to -1, use sum to compare bigger or smaller
- assume each player plays to maximize his score

[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    # top down
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(l, r, turn):
            if l == r:  # terminate
                return nums[l] * turn
            # state transfer: choose l
            lscore = nums[l] * turn + helper(l + 1, r, -turn)
            rscore = nums[r] * turn + helper(l, r - 1, -turn)
            # case1: [8, 3], p1 lscore= 8-3= 5, rscore= 3-8=-5
            # case2: [8, 3], p2 lscore=-8+3=-5, rscore=-3+8= 5
            # why (lscore * turn, rscore * turn):
            # assume each player plays to maximize his score
            return max(lscore * turn, rscore * turn) * turn

        return helper(0, len(nums) - 1, 1) >= 0

    # + mem
    def PredictTheWinner2(self, nums: List[int]) -> bool:
        memory = [[0] * len(nums) for i in range(len(nums))]

        def helper(l, r, turn):
            # terminate
            if l == r:
                return nums[l] * turn
            # memorize
            if memory[l][r] != 0:
                return memory[l][r]
            # state transfer: choose l
            lscore = nums[l] * turn + helper(l + 1, r, -turn)
            rscore = nums[r] * turn + helper(l, r - 1, -turn)
            memory[l][r] = max(lscore * turn, rscore * turn) * turn
            return memory[l][r]

        return helper(0, len(nums) - 1, 1) >= 0
