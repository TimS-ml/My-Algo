# https://leetcode-cn.com/problems/pacific-atlantic-water-flow/


class Solution(object):
    def pacificAtlantic(self, matrix):
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
            self.dfs(i, n-1, a_visited, m, n, matrix)
            
        for j in range(n):
            # up and down
            self.dfs(0, j, p_visited, m, n, matrix)
            self.dfs(m-1, j, a_visited, m, n, matrix)
        #print p_visited, a_visited
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res
    
    def dfs(self, i, j, visited, m, n, matrix):
        visited[i][j] = True
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for dire in direction:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or matrix[i][j] > matrix[x][y]:
                continue
            self.dfs(x, y, visited, m, n, matrix)
            