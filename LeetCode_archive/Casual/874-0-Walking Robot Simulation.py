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
        # check could be ~10,000 times slower if not using set
        obsSet = set(map(tuple, obstacles))
        ans = 0
        for i in range(len(commands)):
            if commands[i] == -2:
                mov = (mov + 1) % 4  # take remainder
            elif commands[i] == -1:
                mov = (mov - 1) % 4
            else:
                for j in range(commands[i]):
                    if (coord[0] + dir[mov][0],
                            coord[1] + dir[mov][1]) not in obsSet:
                        coord[0] += dir[mov][0]
                        coord[1] += dir[mov][1]
                        ans = max(ans,
                                  coord[0] * coord[0] + coord[1] * coord[1])
                    # else:
                    #     print(coord)
                    # coord[0] += commands[i] * dir[mov][0]
                    # coord[1] += commands[i] * dir[mov][1]
        return ans


# commands, obstacles
IN = [([4, -1, 3], []), ([4, -1, 4, -2, 4], [[2, 4]])]
useSet = 1
print(Solution().robotSim(IN[useSet][0], IN[useSet][1]))
