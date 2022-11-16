'''
https://en.wikipedia.org/wiki/Matrix_multiplication

# Code Explain:
sol 1
- Time complexity: O(m k n)
mat1: m x k
mat2: k x n
- Space complexity: O(1)

'''

from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        # Product matrix.
        # m x k @ k x n -> m x n
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        
        # ans[r][c] = mat1[r][i] * mat2[i][c]  for i in range(k)
        for rowID, row in enumerate(mat1):
            # !!! mat1 and mat2 must share the same elementID
            for elementID, row_element in enumerate(row):
                # If current element of mat1 is non-zero then iterate over all columns of mat2.
                if row_element:
                    for colID, col_element in enumerate(mat2[elementID]):
                        ans[rowID][colID] += row_element * col_element
        
        return ans

    # compress
    def multiply_2(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # a list of non-zero val-col pairs
        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
            rows, cols = len(matrix), len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        # Store the non-zero values of each matrix.
        A = compress_matrix(mat1)
        B = compress_matrix(mat2)
        
        ans = [[0] * n for _ in range(m)]
        
        for mat1_row in range(m):
            # Iterate on all current 'row' non-zero elements of mat1.
            # !!! share the same mat1_col
            for element1, mat1_col in A[mat1_row]:
                # Multiply and add all non-zero elements of mat2
                # where the row is equal to col of current element of mat1.
                for element2, mat2_col in B[mat1_col]:
                    ans[mat1_row][mat2_col] += element1 * element2
                    
        return ans
