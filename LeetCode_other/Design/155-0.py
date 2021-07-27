'''
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(n)

# Pros and Cons and Notation:

stack =          [-2,  0, -3]
min_s = [INT_MAX, -2, -2, -3]

The idea is: if -3 is the top of stack, 
    then -2,0,-3 all in stack
    then the min val is -3
'''

import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# O(1) space complexity
class MinStack_2:
    def __init__(self):
        self.stack = []
        self.min_val = -1

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_value = x
        else:
            diff = x - self.min_value
            self.stack.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value
                self.min_value = top - diff
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.stack[-1] < 0 \
            else self.stack[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value if self.stack else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
