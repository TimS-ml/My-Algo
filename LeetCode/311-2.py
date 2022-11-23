'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List
import numpy as np


class Matrix(list):
    def __matmul__(self, B):
        A = self
        return Matrix([[sum(A[i][k] * B[k][j] for k in range(len(B)))
                    for j in range(len(B[0])) ] for i in range(len(A))])

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        return Matrix(mat1) @ Matrix(mat2)

    def multiply_np(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        return np.array(mat1) @ np.array(mat2)

