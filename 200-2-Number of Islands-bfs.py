# https://leetcode-cn.com/problems/number-of-islands/
# https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/


from collections import deque


class Solution:
    # 方向数组
    # 表示相对于当前位置的4个方向的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    

    def numIslands(self, grid) -> int:
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第1行、第1格开始，每格尝试1次BFS
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量
                    # 可以在深度优先遍历self.__dfs完成以后再count
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    # 注意：这里要标记上已经访问过
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        # 得到 4 个方向的坐标
                        for direction in self.directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                #【特别注意】在放入队列以后，要马上标记成已经访问过，语义也是十分清楚的：反正只要进入了队列，你迟早都会遍历到它
                                # 而不是在出队列的时候再标记
                                #【特别注意】如果是出队列的时候再标记，会造成很多重复的结点进入队列，造成重复的操作，这句话如果你没有写对地方，代码会严重超时的
                                marked[new_i][new_j] = True
        return count


grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']]
print(Solution().numIslands(grid))
