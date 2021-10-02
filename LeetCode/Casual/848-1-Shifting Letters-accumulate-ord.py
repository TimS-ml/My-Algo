# https://leetcode-cn.com/problems/shifting-letters/

from typing import List
from itertools import accumulate


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        # need to move: 3+5+9, 5+9, 9
        shifts = list(accumulate(shifts[::-1]))[::-1]
        ans = [
            chr((ord(x) - ord('a') + shifts[i]) % 26 + ord('a'))
            for i, x in enumerate(S)
        ]
        return ''.join(ans)


S = "abc"
shifts = [3, 5, 9]
print(Solution().shiftingLetters(S, shifts))
