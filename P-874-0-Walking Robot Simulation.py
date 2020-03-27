# https://leetcode-cn.com/problems/walking-robot-simulation/
# [1] the movement: list of dir
# [2] obstacles: 
#   how to find
#   stop location (right of obstacle point for example)

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # right, up, left, down, +1 means turn left
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        mov = 1  # init mov upward
        coord = [0, 0]  # init coordinate
        for i in range(len(commands)):
            if commands[i] == -2:
                mov = (mov + 1) % 4  # take remainder
            elif commands[i] == -1:
                mov = (mov - 1) % 4
            elif :
                # coord[0] += commands[i] * dir[mov][0]
                # coord[1] += commands[i] * dir[mov][1]
            else:
                coord[0] += commands[i] * dir[mov][0]
                coord[1] += commands[i] * dir[mov][1]
        return coord


commands1 = [4, -1, 3]
obstacles1 = []

commands2 = [4, -1, 4, -2, 4]
obstacles2 = [[2, 4]]
print(Solution().robotSim(commands2, obstacles2))

