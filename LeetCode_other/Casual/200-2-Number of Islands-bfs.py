# https://leetcode-cn.com/problems/number-of-islands/
# https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/

from collections import deque


class Solution:
    # 方向数组
    # 表示相对于当前位置的4个方向的偏移量, 这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        # 得到 4 个方向的坐标
                        for direct in self.directions:
                            new_i = cur_x + direct[0]
                            new_j = cur_y + direct[1]
                            # same as dfs solution
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[
                                    new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                # 如果是出队列的时候再标记, 会造成很多重复的结点进入队列, 会严重超时
                                marked[new_i][new_j] = True
        return count


grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
print(Solution().numIslands(grid))
