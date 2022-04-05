'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        Y, X = len(matrix), len(matrix[0])
        ans, temp = [], []

        for i in range(X + Y - 1):
            temp.clear()
            # Elements in the first row and the last column are the respective heads.
            # r, c = 0 if i < X else i - X + 1, i if i < X else X - 1
            if i < X:
                r = 0
                c = i
            else:
                r = i - X + 1
                c = X - 1
            print(r, c)

            while r < Y and c > -1:
                temp.append(matrix[r][c])
                r += 1
                c -= 1
            print(temp)

            if i % 2 == 0:
                ans.extend(temp[::-1])  # reverse
            else:
                ans.extend(temp)
        return ans


    def findDiagonalOrder_2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        Y, X = len(matrix), len(matrix[0])
        ans = []

        for i in range(X + Y - 1):
            # Elements in the first row and the last column are the respective heads.
            r = 0 if i < X else i - X + 1
            c = i if i < Y else Y - 1

            if i % 2 == 1:
                for j in range(r, c + 1):
                    ans.append(matrix[j][i - j])  # reverse
            else:
                for j in range(c, r - 1, -1):
                    ans.append(matrix[j][i - j])
        return ans

    def findDiagonalOrder_3(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        Y, X = len(matrix), len(matrix[0])

        ans = []
        dic = defaultdict(list)  # empty dict
        print(dic)

        for i in range(Y):
            for j in range(X):
                # Elements in the first row and the last column are the respective heads.
                dic[i + j + 1].append(matrix[i][j])
            print(dic)

        for i in sorted(dic.keys()):
            if i % 2 == 1:
                dic[i].reverse()  # reverse
            ans.extend(dic[i])
        return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().findDiagonalOrder(matrix))
