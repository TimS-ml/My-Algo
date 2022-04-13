'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Prepare
I have several simple sub function to help me on this kind of problem.

valid(int x, int y), check if (x, y) is valid in the grid.
move(int x, int y), return all possible next position in 4 directions.

Explanation
Only 2 steps:

Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
Loop every cell == 0, check its connected islands and calculate total islands area.
'''

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res
