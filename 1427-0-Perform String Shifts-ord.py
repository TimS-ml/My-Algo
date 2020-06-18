# https://leetcode-cn.com/problems/perform-string-shifts/

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                move += shift[i][1]
            else:
                move -= shift[i][1]
        move = move % len(s)
        return s[move:] + s[:move]


s = "xqgwkiqpif"
shift = [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7],
         [0, 5], [0, 6]]
print(Solution().stringShift(s, shift))
