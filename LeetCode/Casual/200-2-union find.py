'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0:
            return 0

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1),
                                 (r, c + 1)]:
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                            uf.union(r * col + c, x * col + y)

        return uf.getCount()