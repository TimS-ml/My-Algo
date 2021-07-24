'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Pros and Cons and Notation:
case:
"a##c"
"#a#c"

so... list.pop may not be an elegant solution?

for two pointers solution, check:
https://leetcode-cn.com/problems/backspace-string-compare/solution/bi-jiao-han-tui-ge-de-zi-fu-chuan-by-leetcode-solu/
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_out = ''
        t_out = ''
        for i in range(len(s)):
            if s[i] == '#':
                s_out = s_out[:-1]
            else:
                s_out += s[i]
        for i in range(len(t)):
            if t[i] == '#':
                t_out = t_out[:-1]
            else:
                t_out += t[i]
        return s_out == t_out
