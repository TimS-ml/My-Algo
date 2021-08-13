'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

- 与字符串中当前位置的运算符有关
- 如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关
    - 每当遇到一个以 '-' 号开头的括号，则意味着此后的符号都要被「翻转」
'''


class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ans = 0
        L = len(s)
        i = 0
        while i < L:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < L and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ans += num * sign
        return ans
