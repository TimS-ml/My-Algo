'''
# Code Explain:
- Time complexity: O(log(x))
    - There are roughly log(x) digits in x
- Space complexity: O(1)

Convert to string and reverse
And integer should be within the integer range

# Pros and Cons:
## Pros:
- No special cases needed to be concerned (for example 120)

## Cons:

# Notation:
We can use:
    max_int = pow(2, 31) - 1
    min_int = pow(-2, 31)
Instead of -2**31 and 2**31-1
'''


class Solution:
    def reverse(self, x):
        if x >= 0:
            ans = int(str(x)[-1::-1])
        else:
            ans = -int(str(x)[-1:0:-1])
        return ans if -2**31 < ans < 2**31 - 1 else 0


# nums, target
IN = [(123), (-120)]
useSet = 1
print(Solution().reverse(IN[useSet]))
