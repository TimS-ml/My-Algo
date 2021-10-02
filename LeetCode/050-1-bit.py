'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(logN)

https://wiki.python.org/moin/BitwiseOperators

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


x, n = 2, 10
print(Solution().myPow(x, n))
