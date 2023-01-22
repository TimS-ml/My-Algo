'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Why you need 4 directions:
For example "工" shape island
'''

from typing import List
from collections import deque


class Solution:
    # dfs
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(i, j):
            # check the bound!!!
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == '0':
                    return
                if visited[i][j]:
                    return
                
                visited[i][j] = True
                # grid[i][j] = '0'
                
                for x, y in DIR:
                    dfs(i + x, j + y)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # print(grid)
                    ans += 1
                    dfs(i, j)

        # print(grid)
        return ans

    # bfs
    def numIslands_2(self, grid: List[List[str]]) -> int:
        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = deque()
        ans = 0



# grid = [["1","1","1"],
#         ["0","1","0"],
#         ["1","1","1"]]

# grid = [["1","0","1","1","0","1","1"]]

grid = [["0","1","0"],
        ["1","0","1"],
        ["0","1","0"]]

print(Solution().numIslands(grid))
