'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Or you can...
return sum([a, b])

'''

# Integers are not 32-bit in Python !!!

import pysnooper


@pysnooper.snoop()
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000  # MAX_INT + 1
        MASK = 0x100000000  # 2^32
        while b:
            print(bin(a), bin(b))
            # a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


a = 1
b = 2
print(Solution().getSum(a, b))
