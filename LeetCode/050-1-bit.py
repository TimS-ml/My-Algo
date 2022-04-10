'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(logN)

https://wiki.python.org/moin/BitwiseOperators

https://medium.com/@lenchen/leetcode-50-pow-x-n-f4c37c41646d
We can treat n as binary and pick corresponding value into result when corresponding digit is 1. 
For example, if n = 19, it’s binary presentation is 10011, 
which means we can only pick x^(2^0), x^(2^1) and x^(2^4) into result.

- n is odd
- n is even
- n < 0
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
