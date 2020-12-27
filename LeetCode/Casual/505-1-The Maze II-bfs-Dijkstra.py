# https://leetcode-cn.com/problems/the-maze-ii/

import heapq


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        queue = [start]
        m = len(maze)
        n = len(maze[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        pq = [(0, start[0], start[1])]
        while pq:
            count, i, j = heapq.heappop(pq)
            # record
            maze[i][j] = -1
            if i == destination[0] and j == destination[1]:
                return count
            for x, y in dir:
                row = i + x
                col = j + y
                local = 1
                # move until the wall
                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                    row += x
                    col += y
                    local += 1
                # move back a step
                row -= x
                col -= y
                local -= 1
                if maze[row][col] == 0 and [row, col] not in queue:
                    heapq.heappush(pq, (count + local, row, col))
        return -1


maze1 = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]
start1 = [0, 4]
destination1 = [4, 4]

maze2 = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]
start2 = [0, 4]
destination2 = [3, 2]
print(Solution().shortestDistance(maze2, start2, destination2))
