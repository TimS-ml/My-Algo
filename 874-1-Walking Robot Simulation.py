# https://leetcode-cn.com/problems/walking-robot-simulation/
# why this is faster?
# while loop and xxx instead of for loop + if separately
# calculate ans less frequently

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        mov, ans, x, y = 0, 0, 0, 0
        obsSet = set(map(tuple, obstacles))
        for i in range(len(commands)):
            if commands[i] == -2: mov = (mov + 1) % 4
            elif commands[i] == -1: mov = (mov - 1) % 4
            else:
                movx, movy = dir[mov]
                while commands[i] and (x + movx, y + movy) not in obsSet:
                    x += movx
                    y += movy
                    commands[i] -= 1
            ans = max(ans, x**2 + y**2)
        return ans


# commands, obstacles
IN = [([4, -1, 3], []), ([4, -1, 4, -2, 4], [[2, 4]])]
useSet = 1
print(Solution().robotSim(IN[useSet][0], IN[useSet][1]))

