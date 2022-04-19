'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

No '*', '/' !!!

What's different than 227?
We treat everything in (xxx) as an number

The reason we are using list(s) + popleft:
we have recursion
char still loop from left to right
'''

import collections
from typing import List

class Solution:
    def calculate(self, s: str) -> int:      
        def helper(s: List) -> int:
            stack = []
            prevSign = '+'
            num = 0

            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)

                # recursion start
                if c == '(':
                    num = helper(s)

                # new prevSign or last digit
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if prevSign == '+':
                        stack.append(num)
                    elif prevSign == '-':
                        stack.append(-num)
                    elif prevSign == '*':
                        stack[-1] = stack[-1] * num
                    elif prevSign == '/':
                        # python way to write division round to 0
                        stack[-1] = int(stack[-1] / float(num))       
                    num = 0
                    prevSign = c

                # recursion end
                if c == ')':
                    break
            return sum(stack)

        return helper(collections.deque(s))
