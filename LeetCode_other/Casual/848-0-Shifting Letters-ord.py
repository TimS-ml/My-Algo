# https://leetcode-cn.com/problems/shifting-letters/

from typing import List


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        x = sum(shifts) % 26
        S = list(S)
        for i in range(len(S)):
            index = (ord(S[i]) - ord('a') + x) % 26
            S[i] = chr(ord('a') + index)
            x = (x - shifts[i]) % 26
        return ''.join(S)


S = "abc"
shifts = [3, 5, 9]
print(Solution().shiftingLetters(S, shifts))
