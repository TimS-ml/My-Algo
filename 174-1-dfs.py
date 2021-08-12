'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:
https://leetcode-cn.com/problems/dungeon-game/solution/cong-hui-su-dao-ji-yi-hua-sou-suo-dao-dong-tai-gui/

[1] Base State

[2] State Transfer Equation
from (0, 0) to (-1, -1)

[3] Backtrack senario
[4] Initialize Conditions
[5] Terminate Conditions
'''

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        BIG = float('inf')
        cache = [[BIG] * (col + 1) for _ in range(row + 1)]

        def dfs(r, c, cache):
            # Terminate Conditions
            if r >= row or c >= col:
                return BIG
            if cache[r][c] != BIG:
                return cache[r][c]

            # edge case (init case in dp)
            if r == row - 1 and c == col - 1:
                if dungeon[r][c] >= 0:
                    return 0
                else:
                    return -dungeon[r][c]

            # state transfer
            right = dfs(r, c + 1, cache)
            down = dfs(r + 1, c, cache)
            Min = min(right, down) - dungeon[r][c]

            ans = 0
            if Min < 0:
                ans = 0
            else:
                ans = Min
            cache[r][c] = ans
            return ans

        return dfs(0, 0, cache) + 1
