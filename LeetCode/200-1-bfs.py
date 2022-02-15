'''
# Code Explain:
- Time complexity: O(Row * Col)
- Space complexity: O(Row * Col)



https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
'''

from collections import deque


class Solution:
    # left, down, up, right
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0:
            return 0

        marked = [[False for _ in range(col)] for _ in range(row)]
        count = 0

        for i in range(row):
            for j in range(col):
                # a island that not visited
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        for direct in self.directions:
                            new_i = cur_x + direct[0]
                            new_j = cur_y + direct[1]
                            # same as dfs solution
                            if 0 <= new_i < row and \
                               0 <= new_j < col and \
                               not marked[new_i][new_j] and \
                               grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                # 如果是出队列的时候再标记, 会造成很多重复的结点进入队列, 会严重超时
                                marked[new_i][new_j] = True
        return count


grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
print(Solution().numIslands(grid))
