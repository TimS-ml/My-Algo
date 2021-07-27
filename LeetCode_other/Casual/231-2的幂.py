# https://leetcode-cn.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n) -> bool:
        while n > 1:
            n = n / 2

        if n == 1:
            return True
        else:
            return False


print(Solution().isPowerOfTwo(1))
