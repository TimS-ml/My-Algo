'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import deque

class Solution:
    # Use hit to record how many times a 0 grid has been reached
    # and use distSum to record the sum of distance from all 1 grids to this 0 grid.
    # A powerful pruning is that during the BFS we use count1 to count how many 1 grids (building) we reached.
    #   If count1 < buildings then we know not all 1 grids are connected are we can return -1 immediately,
    #   which greatly improved speed (beat 100% submissions).
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        # val in line, line in grid
        buildings = sum(val for line in grid for val in line if val == 1)
        ROW, COL = len(grid), len(grid[0])
        hit, distSum = [[0] * COL for i in range(ROW)], [[0] * COL for i in range(ROW)]

        def BFS(start_x, start_y):
            visited = [[False] * COL for _ in range(ROW)]
            visited[start_x][start_y] = True
            count1, queue = 1, deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < ROW and 0 <= j < COL and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:  # grid == 0
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in range(ROW):
            for y in range(COL):
                # start from 'building'
                if grid[x][y] == 1:
                    if not BFS(x, y):
                        return -1
        ans = []
        for i in range(ROW):
            for j in range(COL):
                if not grid[i][j] and hit[i][j] == buildings:
                    ans.append(distSum[i][j] )
        return min(ans or [-1])


    def shortestDistance_2(self, grid):
        h = len(grid)
        w = len(grid[0])

        distance = [[0 for _ in range(w)] for _ in range(h)]
        reach = [[0 for _ in range(w)] for _ in range(h)]

        buildingNum = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    buildingNum += 1
                    q = [(i, j, 0)]

                    isVisited = [[False for _ in range(w)] for _ in range(h)]

                    for y, x, d in q:
                        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                            r = y + dy
                            c = x + dx

                            if 0 <= r < h and 0 <= c < w and grid[r][c] == 0 and not isVisited[r][c]:
                                distance[r][c] += d + 1
                                reach[r][c] += 1

                                isVisited[r][c] = True
                                q.append((r, c, d + 1))

        shortest = float("inf")
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        if shortest < float("inf"):
            return shortest
        else:
            return -1
