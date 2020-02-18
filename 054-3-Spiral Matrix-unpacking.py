# https://leetcode-cn.com/problems/spiral-matrix/
# https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
# spiral_order([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
# = [1, 2, 3] + spiral_order([[6, 9],
#                             [5, 8],
#                             [4, 7]])
# = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
#                                      [5, 4]])
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(matrix))
