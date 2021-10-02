'''
# Code Explain:
- Time complexity: O(Row * Col)
- Space complexity: O(min(Row, Col))

# Pros and Cons and Notation:

https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
一次dfs可以走完一块island area
'''


class Solution:
    # left, down, up, right
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0:
            return 0

        # dfs标配的记录部分
        marked = [[False for _ in range(col)] for _ in range(row)]
        count = 0

        for i in range(row):
            for j in range(col):
                if not marked[i][j] and grid[i][j] == '1':  # is part of island
                    # count可以理解为连通分量
                    # 可self.dfs完成以后再count
                    count += 1
                    self.dfs(grid, i, j, row, col, marked)
        return count

    def dfs(self, grid, i, j, row, col, marked):
        marked[i][j] = True
        for direct in self.directions:
            new_i = i + direct[0]
            new_j = j + direct[1]
            if 0 <= new_i < row and \
               0 <= new_j < col and \
               not marked[new_i][new_j] and \
               grid[new_i][new_j] == '1':
                self.dfs(grid, new_i, new_j, row, col, marked)


grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
print(Solution().numIslands(grid))
