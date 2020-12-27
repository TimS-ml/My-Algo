# https://leetcode-cn.com/problems/01-matrix/
import collections


class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        def neighbors(r, c):
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= cr < m and 0 <= cc < n:
                    yield cr, cc

        q = collections.deque([((r, c), 0) for r in range(m) for c in range(n)
                               if matrix[r][c] == 0])
        seen = {x for x, _ in q}
        ans = [[0] * n for _ in matrix]
        while q:
            (r, c), depth = q.popleft()
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))

        return ans


matrix1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

matrix2 = [[0, 0, 0], [0, 2, 0], [1, 4, 1]]

print(Solution().updateMatrix(matrix2))
