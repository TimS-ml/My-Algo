'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

- operator needs the number before (that is easy) and after
    - sol: when we find the next operator, we do current calc for prev operator
'''

class Solution:
    def calculate(self, s: str) -> int:
        num, stack = 0, []
        prevSign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            # edge case, last dig
            # Do math operation of prevSign until we meet new sign
            if s[i] in '+-*/' or i == len(s) - 1:
                if prevSign == '+':
                    stack.append(num)
                elif prevSign == '-':
                    stack.append(-num)
                elif prevSign == '*':
                    # stack.append(stack.pop()*num)
                    stack[-1] = stack[-1] * num
                elif prevSign == '/':
                    # stack.append(int(stack.pop()/num))
                    # python way to write division round to 0
                    stack[-1] = int(stack[-1] / float(num))
                num = 0
                prevSign = s[i]

        return sum(stack)  # since '-' is append as -num
