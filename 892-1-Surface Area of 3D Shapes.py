# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/solution/san-wei-xing-ti-de-biao-mian-ji-by-leetcode/


class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2  # top and bottom
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c]-nval, 0)
        return ans
