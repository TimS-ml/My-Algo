# https://leetcode-cn.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()  # function scope var
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res, self.dfs(row, col, grid, seen))
        return res

    def dfs(self, row, col, grid, seen):
        """if a point is valid, it should meet all requirements using "and" """
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (grid[row][col] == 1) and (row, col) not in seen:
            # list this point to seen set so we won't count it again
            seen.add((row, col))
            return (self.dfs(row-1, col, grid, seen) + self.dfs(row+1, col, grid, seen)
                    + self.dfs(row, col-1, grid, seen) +
                    self.dfs(row, col+1, grid, seen)
                    + 1)  # add 1 to the area and DFS(4-Conn Neighbors)
        else:
            return 0  # not valid point return 0
