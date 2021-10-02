'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

Flip + Transpose
'''


class Solution(object):
    def rotate(self, matrix):
        '''
        flip:      [|]
        transpose: [/]

        step1
        [3, 2, 1]
        [6, 5, 4]
        [9, 8, 7]
        
        step2
        3 7 col-1-i = 2
        2 4 col-1-i = 2
        6 8 col-1-i = 1
        
        out
        [7, 4, 1]
        [8, 5, 2]
        [9, 6, 3]
        '''
        if len(matrix) == 0:
            return

        row = col = len(matrix)

        # flip
        for i in range(row):
            for j in range(int(col / 2)):
                idx1 = col - j - 1
                matrix[i][j], matrix[i][idx1] = matrix[i][idx1], matrix[i][j]

        # transpose
        for i in range(row):
            for j in range(col - 1 - i):
                idx1 = col - j - 1
                idx2 = row - i - 1
                matrix[i][j], matrix[idx1][idx2] = matrix[idx1][idx2], matrix[
                    i][j]
        return matrix

    def rotate_2(self, matrix):
        '''
        flip:      [-]
        transpose: [\\]
        '''
        # flip
        matrix.reverse()

        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotate_2(self, matrix):
        '''
        using [::-1] to flip the matrix upside down
        and then zip to transpose it
        '''
        matrix[:] = zip(*matrix[::-1])
        # no zip version, same as version 0
        # but flip first, transpose later
        # matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        print(matrix)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

ans = Solution().rotate_2(matrix)
for row in ans:
    print(row)
