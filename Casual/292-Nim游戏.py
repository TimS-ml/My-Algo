# https://leetcode-cn.com/problems/nim-game/


class Solution:
    def canWinNim(self, n) -> bool:
        return not n % 4 == 0


print(Solution().canWinNim(7))
