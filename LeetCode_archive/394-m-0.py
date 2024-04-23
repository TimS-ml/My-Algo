'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

30[a2[c9d]], 30[2[cd]], 30[a2[cd]]a is not valid

case: 30[a2[cd]]
             |
stak = ['', 30, a, 2, cd]

case: 30[a2[cd]]
              |
stak = [30, acdcd]

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
        # currStr = ''
        # for c in list(s):
        #     if c.isdigit():
        #         dig = dig * 10 + int(c)
        #     elif c.isalpha():
        #         currStr += c
        #     elif c == '[':
        #         stack.append(dig)
        #         dig = 0
        #     elif c == ']':
        #         inner = stack.pop() * stack.pop()
        #         stack[-1] += inner

        stack = []
        dig = 0
        currStr = ''
        for c in s:
            print(stack)
            if c.isdigit():
                dig = dig * 10 + int(c)
            elif c.isalpha():
                currStr += c
            elif c == '[':
                stack.append(currStr)
                stack.append(dig)
                dig = 0
                currStr = ''
            elif c == ']':
                # stack append dig last, so pop it first
                num = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + num*currStr
        return currStr


s = '3[a2[cd]]'
print(Solution().decodeString(s))

