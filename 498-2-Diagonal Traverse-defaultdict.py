# https://leetcode-cn.com/problems/diagonal-traverse/
# https://docs.python.org/3.8/library/collections.html#collections.defaultdict
from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        Y, X = len(matrix), len(matrix[0])

        ans = []
        dic = defaultdict(list)  # empty dict
        print(dic)

        for i in range(Y):
            for j in range(X):
                # Elements in the first row and the last column are the respective heads.
                dic[i+j+1].append(matrix[i][j])
            print(dic)

        for i in sorted(dic.keys()):
            if i % 2 == 1:
                dic[i].reverse()  # reverse
            ans.extend(dic[i])
        return ans


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().findDiagonalOrder(matrix))
