'''
# Code Explain:
- Time complexity: O(2 ^ N)
- Space complexity: O(N)

It is less efficient than BFS because DFS does not guarantee shortest path. We cannot stop after the first valid strings as in BFS.
'''

from functools import lru_cache

class Solution:
    # Generate new strings by removing parenthesis, 
    #   and calculate the total number of mismatched parentheses inside the string by function calc(s).
    # If the mismatched parentheses increased, then discard the string.
    def removeInvalidParentheses(self, s):
        def dfs(s):
            # number of mismatched
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    # remove (skip) s[x]
                    ns = s[:x] + s[x+1:]
                    # if remove s[x] does not increase mismatch
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans    

        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])    
        return dfs(s)

    def removeInvalidParentheses_2(self, s):
        # Generate all valid parentheses start from string s,
        #   we can memoize them to avoid re-compute sub-problem again. 
        #   It's the same idea with 140. Word Break II.
        @lru_cache(None)
        def dfs(i, nOpen):
            # all valid parentheses start from string s
            ans = set()

            # Terminate
            if nOpen < 0:
                return ans  # Invalid, return empty set
            if i == len(s):
                if nOpen == 0: ans.add("")  # Valid: (all paired)
                return ans

            # Case 1: Skip s[i] -> remove???
            if s[i] == '(' or s[i] == ')':
                # set.update(iterable)
                ans.update(dfs(i + 1, nOpen))

            # Case 2: Include s[i]: '(', ')'
            # if we want to include s[i], then we need to update nOpen first
            if s[i] == '(':
                nOpen += 1
            elif s[i] == ')':
                nOpen -= 1
            for suffix in dfs(i + 1, nOpen):
                ans.add(s[i] + suffix)
            return ans

        # Then get the maximum length among those valid parentheses.
        # Filter the result by choosing parentheses which has the length **equals to** the maximum length.
        validParentheses = dfs(0, 0)
        maxLen = max(map(len, validParentheses))
        return filter(lambda x: len(x) == maxLen, validParentheses)

