'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Yale format.
Yale format or Compressed Sparse Row (CSR)

'''

from typing import List


class SparseMatrix:
    def __init__(self, matrix: List[List[int]], col_wise: bool):
        self.values, self.row_index, self.col_index = self.compress_matrix(matrix, col_wise)

    def compress_matrix(self, matrix: List[List[int]], col_wise: bool):
        return self.compress_col_wise(matrix) if col_wise else self.compress_row_wise(matrix)

    # Compressed Sparse Row
    def compress_row_wise(self, matrix: List[List[int]]):
        values = []
        row_index = [0]
        col_index = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    col_index.append(col)
            row_index.append(len(values))

        return values, row_index, col_index

    # Compressed Sparse Column
    def compress_col_wise(self, matrix: List[List[int]]):
        values = []
        row_index = []
        col_index = [0]

        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    row_index.append(row)
            col_index.append(len(values))

        return values, row_index, col_index

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
            A = SparseMatrix(mat1, False)
            B = SparseMatrix(mat2, True)
            
            ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

            for row in range(len(ans)):
                for col in range(len(ans[0])):

                    # Row element range indices
                    mat1_row_start = A.row_index[row]
                    mat1_row_end = A.row_index[row + 1]

                    # Column element range indices
                    mat2_col_start = B.col_index[col]
                    mat2_col_end = B.col_index[col + 1]
                    
                    # Iterate over both row and column.
                    while mat1_row_start < mat1_row_end and mat2_col_start < mat2_col_end:
                        if A.col_index[mat1_row_start] < B.row_index[mat2_col_start]:
                            mat1_row_start += 1
                        elif A.col_index[mat1_row_start] > B.row_index[mat2_col_start]:
                            mat2_col_start += 1
                        # Row index and col index are same so we can multiply these elements.
                        else:
                            ans[row][col] += A.values[mat1_row_start] * B.values[mat2_col_start]
                            mat1_row_start += 1
                            mat2_col_start += 1
    
            return ans
