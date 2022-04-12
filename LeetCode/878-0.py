'''
# Code Explain:
- Time complexity: O(log(N x min(A, B)))
- Space complexity: O(1)

[1] Get gcd (greatest common divisor) and lcm (least common multiple) of (A, B).
(a, b) = (A, B) while b > 0: (a, b) = (b, a % b)
then, gcd = a and lcm = A * B / a

[2] How many magic numbers <= x ?
By inclusion exclusion principle, we have:
x / A + x / B - x / lcm

[3] Set our binary search range
Lower bound is min(A, B), I just set left = 2.
Upper bound is N * min(A, B), I just set right = 10 ^ 14.

[4] Binary search, find the smallest x that x / A + x / B - x / lcm = N

'''

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        def getGCD(x, y):
            while y > 0:
                x, y = y, x % y
            return x

        def getLCM(x, y, gcd):
            return x * y // gcd

        def numBelow(x):
            return (x // A) + (x // B) - (x // lcm)
        
        gcd = getGCD(A, B)
        lcm = getLCM(A, B, gcd)
        
        left = 0
        right = N * min(A, B) 
        
        while left < right:
            mid = (left + right) // 2
            
            if numBelow(mid) < N:
                left = mid + 1
            else:
                right = mid
        return left % (10**9+7)

