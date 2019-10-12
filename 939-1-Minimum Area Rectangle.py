# https://leetcode-cn.com/problems/minimum-area-rectangle/
# sides parallel to the x and y axes
# 这个code表达很乱


import matplotlib.pyplot as plt
from collections import defaultdict


class Solution:
    def minAreaRect(self, points) -> int:

        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        # columns = {}
        # for i in range(len(points)):
        #     if points[i][0] in columns.keys():
        #         columns[points[i][0]].append(points[i][1])
        #     else:
        #         columns[points[i][0]] = [points[i][1]]

        last_x = {}
        ans = float('inf')
        print(columns)
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in last_x:
                        ans = min(ans, (x-last_x[y1, y2])*(y2-y1))
                    last_x[y1, y2] = x
        return ans if ans < float('inf') else 0


points1 = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
points2 = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]

# x, y = [], []
# for i in range(len(points1)):
#     x.append(points1[i][0])
#     y.append(points1[i][1])
# print(x, y)

# plt.plot(x, y, 'o')
# plt.show()

print(Solution().minAreaRect(points1))
