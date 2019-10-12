# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
# 每一次找到递增的时候，继续DFS，然后用cache来记录每一个（i，j）最大可能的递增长度


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        cache = [[0 for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(i, j, cache, matrix))
        return ans

    def dfs(self, i, j, cache, matrix):
        # find cache
        if cache[i][j] != 0:
            return cache[i][j]
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dire in direction:
            x, y = i+dire[0], j+dire[1]
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[i][j] >= matrix[x][y]:
                continue
            cache[i][j] = max(cache[i][j], self.dfs(x, y, cache, matrix))
        # self (i,j) + 1
        cache[i][j] += 1
        return cache[i][j]
