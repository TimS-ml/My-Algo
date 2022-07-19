'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 832
'''


def flip_an_invert_image(matrix):
    C = len(matrix)
    for row in matrix:
        for i in range((C + 1) // 2):
            row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1

    return matrix


def main():
    print(flip_an_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(
        flip_an_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1],
                              [1, 0, 1, 0]]))


main()
