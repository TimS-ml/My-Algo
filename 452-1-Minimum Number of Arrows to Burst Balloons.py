# https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    def findMinArrowShots(self, points) -> int:
        ans = 0
        points.sort(key=lambda p:p[1])
        print(points)
        end = float("-inf")
        for s, e in points:
            if s>end:
                ans += 1
                end = e
        return ans


points1 = [[10,16], [2,8], [1,6], [7,12]]
points2 = [[10,11], [2,8], [1,6], [7,12]]
print(Solution().findMinArrowShots(points2))
