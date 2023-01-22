'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

30[a2[c9d]] is not valid
case: 30[a2[cd]], 30[2[cd]], 30[a2[cd]]a
stak = [30, a, 2, cd] -> [30, acdcd]

collect all the digs before [
collect all the chars after [
    - until dig or ]
if ]:
    do dig * str, append result to stack

'''

class Solution:
    # ok you should clear your logic
    def decodeString(self, s: str) -> str:
        # stack = []

        # dig = 0
        # repeatStr = ''
        # ans = ''
        # for c in list(s):
        #     if c.isdigit():
        #         dig = dig * 10 + int(c)
        #     elif c.isalpha():
        #         repeatStr += c
        #     elif c == '[':
        #         stack.append(dig)
        #         dig = 0
        #     elif c == ']':
        #         inner = stack.pop() * stack.pop()
        #         stack[-1] += inner

        stack = []

        dig = 0
        repeatStr = ''
        ans = ''
        for c in list(s):
            if c.isdigit():
                dig = dig * 10 + int(c)
            elif c.isalpha():
                repeatStr += c
            elif c == '[':
                stack.append(dig)
                dig = 0
            elif c == ']':
                inner = stack.pop() * stack.pop()
                stack[-1] += inner
