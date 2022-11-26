'''
# Code Explain:
- Time complexity: O(MN)
- Space complexity: O(MN)

M is the number of rows and NN is the number of columns.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
            ):
                return
            
            if heights[r][c] >= prevHeight:
                visit.add((r, c))
            else:
                return
            
            for movI, movJ in direction:
                dfs(r + movI, c + movJ, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        return set.intersection(pac, atl)


    def pacificAtlantic_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(MN)
        # need to write more
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])

        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]

        res = []
        for i in range(m):
            # left and right

            self.dfs(i, 0, p_visited, m, n, matrix)
            self.dfs(i, n - 1, a_visited, m, n, matrix)

        for j in range(n):
            # up and down
            self.dfs(0, j, p_visited, m, n, matrix)
            self.dfs(m - 1, j, a_visited, m, n, matrix)
        # print p_visited, a_visited
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, i, j, visited, m, n, matrix):
        visited[i][j] = True
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dire in direction:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][
                    y] or matrix[i][j] > matrix[x][y]:
                continue
            self.dfs(x, y, visited, m, n, matrix)

