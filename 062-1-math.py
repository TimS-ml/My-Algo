'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

The number of possible paths the robot can take is then the binomial coefficient 
C(m-1, m+n-2) = B(m+n-2,m-1) = factorial(m+n-2)/(factorial(m-1)*factorial(n-1))
Read as m-1 choose m+n-2

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from math import factorial


class Solution(object):
    def uniquePaths(self, m, n):
        return int(
            factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))
