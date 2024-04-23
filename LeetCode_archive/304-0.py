'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])

        # sum[i][j] is sum of all elements inside the rectangle [0,0,i,j]
        self.sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.sum[r][c] = self.sum[r - 1][c] + \
                                 self.sum[r][c - 1] - \
                                 self.sum[r - 1][c - 1] + \
                                 matrix[r - 1][c - 1]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # Since our `sum` starts by 1 so we need to increase r1, c1, r2, c2 by 1
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        return self.sum[r2][c2] - \
               self.sum[r2][c1 - 1] - \
               self.sum[r1 - 1][c2] + \
               self.sum[r1 - 1][c1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
