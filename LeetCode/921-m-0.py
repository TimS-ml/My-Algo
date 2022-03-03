'''
# Code Explain:
Sol 2
- Time complexity: O(N)
- Space complexity: O(N)

Sol 2:
balance = -1 means ) no (: take action, then reset balance
balance >0 means one or more (: continue looping

case: )(
step1:
    balance = -1
    anction = 1
    balance = 0
step2:
    balance = 1
    anction = 1
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)

    def minAddToMakeValid_2(self, s: str) -> int:
        anction = balance = 0
        for symbol in s:
            if symbol == '(':
                balance += 1
            else:
                balance -= 1
            if balance == -1:  # ')'
                anction += 1
                balance += 1
        return anction + balance
