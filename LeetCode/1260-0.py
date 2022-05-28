'''
# Code Explain:
- Time complexity: O(ROWxCOL)
- Space complexity: O(1)

- Index mapping
  - A elegant way is to use 'mod'
  - How to convert ROWxCOL 2d array <=> 1d array
'''


class Solution:
    def shiftGrid(self, grid, k):
        ROW, COL = len(grid), len(grid[0])

        # 2d idx => 1d idx
        def pos2val(r, c):
            return r * COL + c

        # 1d idx => 2d idx
        def val2pos(v):
            return [v // COL % ROW, v % COL]  # r, c

        # init an empty 2d list
        ans = [[0] * COL for _ in range(ROW)]

        for r in range(ROW):
            for c in range(COL):
                newIdx1d = pos2val(r, c) + k % (ROW * COL)  # include shifting
                newR, newC = val2pos(newIdx1d)
                print(f'[{r}, {c}], newIdx1d: {newIdx1d}, new: [{newR}, {newC}]')
                ans[newR][newC] = grid[r][c]

        return ans


grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
k = 2
print(Solution().shiftGrid(grid, k))
