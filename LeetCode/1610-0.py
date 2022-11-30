'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

Here are the steps:
- convert all coordinates to radians
- sort the array
- use sliding window to find the longest window that satisfies arr[r] - arr[l] <= angle.

Note that we need to go around the circle, so we duplicate the array and offset the second half by 2*pi.

https://leetcode.com/problems/maximum-number-of-visible-points/discuss/894732/Python-C%2B%2B-3-Simple-Steps
'''

import math
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        if not points or len(points) == 0:
            return 0
        
        pointsAtLocationCount = 0
        pointsAngles = []
        
        for x, y in points:
            dx = x - location[0]
            dy = y - location[1]
            if dx == 0 and dy == 0:
                pointsAtLocationCount += 1
            else:
                radAngle = math.atan2(dy, dx)
                degAngle = math.degrees(radAngle)
                pointsAngles.append(degAngle)
        
        pointsAngles = sorted(pointsAngles)

        # Add the additional points to handle points in the angle but separated by the east axis. 
        pointsAngles += [i+360 for i in pointsAngles]
        
        l = 0
        res = 0
        for r in range(len(pointsAngles)):
            while(pointsAngles[r] - pointsAngles[l] > angle):
                l += 1
            res = max(res, r-l+1)

        # Add the points those are at the location and return.
        return res + pointsAtLocationCount
