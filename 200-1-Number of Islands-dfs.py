# https://leetcode-cn.com/problems/number-of-islands/
# https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/


class Solution:
    # 方向数组
    # 表示相对于当前位置的4个方向的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        # 从第1行、第1格开始，每格尝试1次DFS
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量
                    # 可以在深度优先遍历self.__dfs完成以后再count
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
        return count


    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)


grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']]
print(Solution().numIslands(grid))
