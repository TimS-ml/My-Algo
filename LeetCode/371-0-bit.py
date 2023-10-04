'''
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(1)

# a is int, convert decimal to binary
'{0:b}'.format(a)
bin(a)

'''

# Integers are not 32-bit in Python !!!

import pysnooper


@pysnooper.snoop()
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF  # bitmask of 31 1-bits
        MIN_INT = 0x80000000  # MAX_INT + 1
        MASK = 0x100000000  # 2^32
        while b:
            print(bin(a), bin(b))
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
            # carry = (a & b) << 1
            # a = (a ^ b) % MASK
            # b = carry % MASK

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        # return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
        return a if a < MAX_INT else ~(a ^ MASK)

    # this is not good, it uses the multiplication
    def getSum_2(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign


a = 1
b = 2
print(Solution().getSum(a, b))
