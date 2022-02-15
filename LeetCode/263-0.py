'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)


- num > 0
'''


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for f in factors:
            while n % f == 0:
                n //= f

        return n == 1
