# https://leetcode-cn.com/problems/the-maze/


class Solution(object):
    def hasPath(self, maze, start, destination):
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
        while queue:
            i, j = queue.pop(0)
            maze[i][j] = -1
            if i == destination[0] and j == destination[1]:
                return True
            for x, y in dir:
                row = x + i
                col = y + j
                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0 and [row, col] not in queue:
                    queue.append([row, col])
        return False


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
