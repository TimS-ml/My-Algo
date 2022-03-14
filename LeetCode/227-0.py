'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

- operator needs the number before (that is easy) and after
    - sol: when we find the next operator, we do current calc
'''

class Solution:
    def calculate(self, s: str) -> int:
        # sign is previous operator
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            # edge case, last dig
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]

        return sum(stack)  # since '-' is append as -num
