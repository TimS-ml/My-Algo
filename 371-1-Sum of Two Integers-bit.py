# https://leetcode-cn.com/problems/sum-of-two-integers/
# https://wiki.python.org/moin/BitwiseOperators
# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

# How do we check if only one bit is 1? Use ^.
# How do we check if both bits are 1? Use &.

'''
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

~ x
https://en.wikipedia.org/wiki/Two%27s_complement
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

x ^ y exclusive OR
https://en.wikipedia.org/wiki/XOR_gate
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
'''

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

