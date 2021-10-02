'''
# Code Explain:
- Time complexity: O(mn)
- Space complexity: O(1)

# Pros and Cons and Notation:
- m[i][i] remains the same
'''

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]
        return ans


matrix = [[1, 2, 3], [4, 5, 6]]
print(Solution().transpose(matrix))
