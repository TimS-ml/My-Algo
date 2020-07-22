'''
# Code Explain:
- Time complexity: O(log(x))
    - There are roughly log(x) digits in x
- Space complexity: O(1)

No overflow needed to be check in python

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class Solution:
    def reverse(self, x):
        # sign = cmp(x, 0)  # only in python 2.x
        sign = -1 if x < 0 else 1

        x = abs(x)
        ans = 0

        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10

        return ans*sign if -2**31 < ans*sign < 2**31 - 1 else 0


# nums, target
IN = [
    (123), 
    (-120)
]
useSet = 1
print(Solution().reverse(IN[useSet]))

