# https://leetcode-cn.com/problems/rotate-image/
# 实现顺时针90度的旋转效果:
# 沿水平中线上下翻转（-180° + 一次镜像）
# 沿右上 - 左下的对角线翻转（270° + 一次镜像）


class Solution(object):
    def rotate(self, matrix):
        if len(matrix) == 0:
            return

        h = w = len(matrix)  # h是纵列

        # 沿中轴线翻转
        for i in range(0, h):
            for j in range(0, int(w/2)):  # 3*3数组：int(w/2)=1，相当只进行了j=0这一组
                # print(matrix[i])
                # print(matrix[i][j], matrix[i][w-j-1])  # w-j-1=2
                matrix[i][j], matrix[i][w-j-1] = matrix[i][w-j-1], matrix[i][j]
                # print(matrix[i])

        # for i in range(len(matrix)):
        #     print(matrix[i])

        # 沿左下-右上的对角线翻转
        for i in range(0, h):
            for j in range(0, w-1-i):
                print(matrix[i][j], matrix[w-1-j][h-1-i], 'w-1-i =', w-1-i)
                matrix[i][j], matrix[w-1-j][h-1-i] = matrix[w-1-j][h-1-i], matrix[i][j]
        
        # for i in range(len(matrix)):
        #     print(matrix[i])


matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

# step1
# [3, 2, 1]
# [6, 5, 4]
# [9, 8, 7]

# step2
# 3 7 w-1-i = 2
# 2 4 w-1-i = 2
# 6 8 w-1-i = 1

# out
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

Solution().rotate(matrix)
