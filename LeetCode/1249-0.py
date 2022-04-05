'''
# Code Explain:
sol 1
- Time complexity: O(N)
- Space complexity: O(N)

'''

class Solution:
    # use one pass + stack
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []  # save idx for `(` only

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)  # append idx !!!
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # a clever way to remove str

        while stack:
            s[stack.pop()] = ''  # remove `(` based on idx
        return ''.join(s)

    # two pass without stack
    def minRemoveToMakeValid_2(self, s: str) -> str:
        del_idx = set()
        stack = []  # save idx for `(` only

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:  # `)`
                    del_idx.add(i)
                else:
                    stack.pop()

        del_idx = del_idx.union(set(stack))  # idx of `(` and `)`
        ans = []
        for i, c in enumerate(s):
            if i not in del_idx:
                ans.append(c)

        return ''.join(ans)
