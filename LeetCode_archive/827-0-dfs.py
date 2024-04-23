'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Prepare
I have several simple sub function to help me on this kind of problem.

valid(int x, int y), check if (x, y) is valid in the grid.
move(int x, int y), return all adjacentIdx next position in 4 directions.

Explanation
Only 2 steps:

Explore every island using DFS, count its area, give it an island idx and save the result to a {idx: area} map.
Loop every cell == 0, check its connected islands and calculate total islands area.
'''

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, idx):
            ans = 0
            grid[x][y] = idx
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    ans += dfs(i, j, idx)
            return ans + 1

        # DFS every island and give it an idx of island
        idx = 2  # since grid contains 0 and 1

        # !!! init 0 idx with val=0 !!!
        sizeDict = {0: 0}  # idx: size
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    sizeDict[idx] = dfs(x, y, idx)
                    idx += 1

        # traverse every 0 cell and count biggest island it can conntect
        ans = max(sizeDict.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    # set(grid[i][j]) contains all the adjacent islands' idx
                    adjacentIdx = set(grid[i][j] for i, j in move(x, y))

                    # remember + 1!!!
                    # since sizeDict[0]=0, grid[i][j]=0 will not affect result
                    ans = max(ans, sum(sizeDict[idx] for idx in adjacentIdx) + 1)
        return ans
