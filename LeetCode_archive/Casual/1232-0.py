'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)


check if dy/dx = k for every c[0] and c[i!=0]

special case:
- dx==0 or dy==0
- point overlap

we can move the line to orignal point
'''

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        dy = coordinates[0][1] - coordinates[1][1]
        dx = coordinates[0][0] - coordinates[1][0]

        if dy == 0:
            for i in range(2, len(coordinates)):
                curr_dy = coordinates[0][1] - coordinates[i][1]
                if curr_dy != 0:
                    return False
        elif dx == 0:
            for i in range(2, len(coordinates)):
                curr_dx = coordinates[0][0] - coordinates[i][0]
                if curr_dx != 0:
                    return False
        else:
            k = dy / dx
            for i in range(2, len(coordinates)):
                curr_dy = coordinates[0][1] - coordinates[i][1]
                curr_dx = coordinates[0][0] - coordinates[i][0]

                if curr_dy == 0 or curr_dx == 0:
                    if curr_dx == curr_dy:
                        continue
                    else:
                        return False
                if curr_dy / curr_dx != k:
                    return False

        return True

    def checkStraightLine_2(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        dy = coordinates[0][1] - coordinates[1][1]
        dx = coordinates[0][0] - coordinates[1][0]

        for i in range(2, len(coordinates)):
            curr_dy = coordinates[0][1] - coordinates[i][1]
            curr_dx = coordinates[0][0] - coordinates[i][0]

            if curr_dy * dx - curr_dx * dy != 0:
                return False

        return True

    def checkStraightLine_3(self, coordinates: List[List[int]]) -> bool:
        # move the point c[0] to orignal point
        dy = coordinates[0][1]
        dx = coordinates[0][0]
        for i in range(len(coordinates)):
            coordinates[i][1] -= dy
            coordinates[i][0] -= dx

        # y/x = curr_y/curr_x <=> curr_x*y - curr_y*x = 0
        # which remove the zero check
        y = coordinates[1][1]
        x = -coordinates[1][0]
        for i in range(2, len(coordinates)):
            if y * coordinates[i][0] + x * coordinates[i][1] != 0:
                return False

        return True
