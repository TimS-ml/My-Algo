# https://leetcode-cn.com/problems/sum-of-two-integers/
# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
# https://leetcode.com/problems/sum-of-two-integers/discuss/167931/Solution-with-ACTUAL-explanation-(how-you-would-work-this-out)


class Solution:
    def getSum(self, a: int, b: int) -> int:
        print(bin(a), bin(b))
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


a = 1
b = 2
print(Solution().getSum(a, b))

