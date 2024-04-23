'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

neet to go through every 0 once
'''

from typing import List


class Solution:
    def uniquePathsIII(self, A):
        ans = 0
        R, C, empty = len(A), len(A[0]), 1

        initX, initY = 0, 0
        for i in range(R):
            for j in range(C):
                if A[i][j] == 1:
                    initX, initY = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        # visited = set()
        # use empty to prevent early stopping
        def dfs(x, y, empty):
            nonlocal ans

            # < 0 include visited
            if not (0 <= x < R and 0 <= y < C and A[x][y] >= 0):
                return
            if A[x][y] == 2:
                ans += empty == 0
                return

            # backtracking
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0

        dfs(initX, initY, empty)
        return ans
