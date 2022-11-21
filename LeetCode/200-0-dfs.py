'''
# Code Explain:
- Time complexity: O(Row * Col)
- Space complexity: O(min(Row, Col))

'''


class Solution:
    # left, down, up, right
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0:
            return 0
        visited = [[False for _ in range(col)] for _ in range(row)]

        # def dfs(i, j):
        #     visited[i][j] = True
        #     for direct in self.directions:
        #         new_i = i + direct[0]
        #         new_j = j + direct[1]
        #         if 0 <= new_i < row and \
        #            0 <= new_j < col and \
        #            not visited[new_i][new_j] and \
        #            grid[new_i][new_j] == '1':
        #             dfs(new_i, new_j)
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if grid[i][j] == '0':
                return
            if visited[i][j]:
                return

            visited[i][j] = True
            for direct in self.directions:
                new_i = i + direct[0]
                new_j = j + direct[1]
                dfs(new_i, new_j)

        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':  # is part of island
                    # count可以理解为连通分量
                    # 可self.dfs完成以后再count
                    count += 1
                    dfs(i, j)
        return count



grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
print(Solution().numIslands(grid))
