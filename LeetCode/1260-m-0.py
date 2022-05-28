'''
# Code Explain:
- Time complexity: O(ROWxCOL)
- Space complexity: O(1)

- A elegant way is to use 'mod'
- How to convert ROWxCOL 2d array <=> 1d array
'''


class Solution:
    def shiftGrid(self, grid, k):
        ans = []
        for subarr in grid:
            ans.extend(subarr)
        return ans[-k:] + ans[:-2]


grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
k = 2
print(Solution().shiftGrid(grid, k))

