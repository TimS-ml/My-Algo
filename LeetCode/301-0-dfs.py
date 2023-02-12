'''
# Code Explain:
- Time complexity: O(N * 2 ^ N)
- Space complexity: O(N)

Break into 3 parts, l = '(', r = ')'
# [1] Check whether a input str is valid
- l == r
- check if current r < l

# [2] Compute min number of l and r to remove
case:
"(a)())()", l = 3, r = 4, you can delete ANY ')'
"(a()" -> "a()" and "(a)"
")()" -> must remove first r!

# [3] Generate all the combo

'''

from functools import lru_cache

class Solution:
    def removeInvalidParentheses(self, s):
        # init l, r needed to be removed
        l, r = 0, 0
        for c in s:
            l += (c == '(')
            if l == 0:
                r += (c == ')')
            else:
                l -= (c == ')')
        # print(l, r)

        ans = []

        def isValid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0
        
        def dfs(subStr, idx, l, r):
            if l == 0 and r == 0:
                if isValid(subStr):
                    ans.append(subStr)
                return

            for i in range(idx, len(subStr)):
                if i != idx and subStr[i] == subStr[i-1]:
                    continue

                if subStr[i] in '()':
                    if r > 0 and subStr[i] == ')':
                        curr = subStr[:i] + subStr[i+1:]
                        dfs(curr, i, l, r-1)
                    elif l > 0 and subStr[i] == '(':
                        curr = subStr[:i] + subStr[i+1:]
                        dfs(curr, i, l-1, r)
        
        dfs(s, 0, l, r)
        return ans

    # terrible but valid solution:
    # Generate new strings by removing parenthesis,
    #   and calculate the total number of mismatched parentheses inside the string by function calc(s).
    # If the mismatched parentheses increased, then discard the string.
    # string slicing made this super slow
    # also might recompute sub-problems
    def removeInvalidParentheses_2(self, s):
        def dfs(s):
            # number of mismatched
            mismatch = calcMismatch(s)
            if mismatch == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    # remove (skip) s[x]
                    ns = s[:x] + s[x+1:]
                    # if remove s[x] does not increase mismatch
                    if ns not in visited and calcMismatch(ns) < mismatch:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans

        def calcMismatch(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])
        return dfs(s)

    # terrible but valid solution:
    # GENERATE all valid parentheses start from string s,
    #   we can memoize them to avoid re-compute sub-problem again.
    # It's the same idea with 140. Word Break II.
    # Will generate all the possible combos at any length
    # Need to filter out the correct length substr then return 
    def removeInvalidParentheses_3(self, s):
        @lru_cache(None)
        def dfs(i, nOpen):
            # all valid parentheses start from string s
            ans = set()

            # Terminate
            if nOpen < 0:
                return ans  # Invalid, return empty set
            if i == len(s):
                # Valid: (all paired), return empty string
                #   then perform string generation
                # if invalid, then return None
                if nOpen == 0:
                    ans.add("")
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



s = ")((()"
print(Solution().removeInvalidParentheses(s))
