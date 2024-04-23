'''
# Code Explain:
- Time complexity: O(log(x))
    - There are roughly log(x) digits in x
- Space complexity: O(1)

Convert to string and reverse
And integer should be within the integer range

We can use:
    max_int = pow(2, 31) - 1
    min_int = pow(-2, 31)
Instead of -2**31 and 2**31-1
'''

import math


class Solution:
    # def reverse(self, x):
    #     if x >= 0:
    #         ans = int(str(x)[-1::-1])
    #     else:
    #         ans = -int(str(x)[-1:0:-1])
    #     return ans if -2**31 < ans < 2**31 - 1 else 0

    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        ans = 0
        while x:
            digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            if ans > MAX // 10 or (ans == MAX // 10 and digit > MAX % 10):
                return 0
            if ans < MIN // 10 or (ans == MIN // 10 and digit < MIN % 10):
                return 0
            ans = (ans * 10) + digit

        return ans

    def reverse_2(self, x):
        # sign = cmp(x, 0)  # only in python 2.x
        sign = -1 if x < 0 else 1

        x = abs(x)
        ans = 0

        while x != 0:
            # print(x, ans)
            ans = ans * 10 + x % 10
            x //= 10

        return ans * sign if -2**31 < ans * sign < 2**31 - 1 else 0


# nums, target
IN = [(123), (-120)]
useSet = 1
print(Solution().reverse(IN[useSet]))
