# https://leetcode-cn.com/problems/power-of-three/
# 用到了数论的知识
# 3的幂次的质因子只有3
# 而所给出的n如果也是3的幂次
# 故而题目中所给整数范围内最大的3的幂次的因子只能是3的幂次
# 1162261467是3的19次幂, 是整数范围内最大的3的幂次


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            return (1162261467 % n) == 0
        else:
            return False
