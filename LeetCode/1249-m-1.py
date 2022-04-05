'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

n
if (
    += 1

if )
    n[-1]

lee(t(c)o)de)
a)b(c)d

()(((((
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        i = 0

        n = 0
        position = 0
        while i < len(s):
            if s[i] == '(':
                n += 1
            elif s[i] == ')':
                if n <= 0:
                    s.remove(i)  # remove )
                    i -= 1
                else:
                    n -= 1
            if n == 0:
                position = i
            i += 1

        i = position + 1
        while n > 0:
            if s[i] == '(':
                s.remove(i)
                n -= 1

        return ''.join(s)
