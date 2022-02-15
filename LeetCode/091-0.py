'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n) or O(1)



decode in to a list of num<=26
- 1 or 2 dig split
number should not start with 0 (case: 06)

dp[i]:
num of ways to be decode for s[:i+1]

state transfer:
if i-1 != 0
'xx26' = ('xx', 26) + ('xx2', 6)
dp[i] = dp[i-1] + dp[i-2]

if i-1 == 0
'xx26' = invalid: ('xx', 06) + ('xx2', 6)
dp[i] = dp[i-2]

init: 
d[0] and dp[1]

state compresstion:
...
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        L = len(s)
        f = [1] + [0] * L
        for i in range(1, L + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[L]

    # state compress
    def numDecodings_2(self, s: str) -> int:
        L = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, L + 1):
            c = 0
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                c += a
            a, b = b, c
        return c
