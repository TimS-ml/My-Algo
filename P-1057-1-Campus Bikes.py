# https://leetcode-cn.com/problems/campus-bikes/
# pending...


class Solution:
    def Manhattan(self, l1_x, l1_y, l2_x, l2_y):
        x = abs(l1_x - l2_x)
        y = abs(l1_y - l2_y)
        # print(x+y)
        return x + y

    def assignBikes(self, workers, bikes):
        ans = []
        worker_num = 0
        bike_num = 0
        min_distance = 100000
        # while bikes:
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distance = self.Manhattan(workers[i][0], workers[i][1],
                                          bikes[bike_num][0],
                                          bikes[bike_num][1])
                if distance < min_distance:
                    min_distance = distance

            print(i, distance)


# [1,0]
workers1 = [[0, 0], [2, 1]]
bikes1 = [[1, 2], [3, 3]]

# [0,2,1]
workers2 = [[0, 0], [1, 1], [2, 0]]
bikes2 = [[1, 0], [2, 2], [2, 1]]

print(Solution().assignBikes(workers1, bikes1))
