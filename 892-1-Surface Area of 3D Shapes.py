# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/solution/san-wei-xing-ti-de-biao-mian-ji-by-leetcode/
# We only calculate the cube higher than it's surroundings


class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)
        ans = 0
        for row in range(N):
            for col in range(N):
                if grid[row][col]:
                    ans += 2  # top and bottom
                    dirs = ((row-1, col), (row+1, col),
                            (row, col-1), (row, col+1))
                    for nrow, ncol in dirs:
                        if 0 <= nrow < N and 0 <= ncol < N:
                            value = grid[nrow][ncol]
                        else:
                            value = 0
                        ans += max(grid[row][col]-value, 0)
        return ans


grid = [[1, 2], [3, 4]]
print(Solution().surfaceArea(grid))
