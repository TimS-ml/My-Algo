'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

stack, pattern: num, num, sign
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return stack.pop()

    def evalRPN_2(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                r, l = str(stack.pop()), str(stack.pop())
                stack.append(int(eval(l+t+r)))
        return stack.pop()
