# https://leetcode-cn.com/problems/power-of-three/
# 想法很好……但是开根号的结果不是很靠谱
# 用if n == math.pow(3, y)这种倒是可以


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n == 0:
            return False
        x = math.pow(n, 1 / 3)
        print(x)
        return isinstance(x, int)


print(Solution().isPowerOfThree(8))
