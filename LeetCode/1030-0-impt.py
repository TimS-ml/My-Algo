'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int,
                          cCenter: int) -> List[List[int]]:
        ans = [(i, j) for i in range(rows) for j in range(cols)]
        ans.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return ans
