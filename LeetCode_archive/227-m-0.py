'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

skip space

stack of num
stack of op

if  * or /
pop number and op

case
1 * 2 * 3
22+1

'''

class Solution:
    def calculate(self, s: str) -> int:
        ops = []
        nums = []

        i = 0
        while i < len(s):
            calc = False
            if s[i].isdigit():
                num = 0
                while s[i].isdigit():
                    i += 1
                    num = num * 10 + int(s[i])
                nums.append(num)
            if s[i].isalpha():
                if s[i] == '+' or s[i] == '-':
                    ops.append(s[i])
                    i += 1
