'''
# Code Explain:
- Time complexity: O(2 ^ N)
- Space complexity: O(N)

'''

from functools import lru_cache

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:
            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                if left == 0:
                    right += 1

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                if left > 0:
                    left -= 1

        ans = []
        # left_count, right_count is to check if valid
        def dfs(idx, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if idx == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans.append("".join(expr))
            else:
                # The discard case. Note that here we have our pruning condition.
                # We don't remove if the remaining count for that parenthesis is == 0.
                if (s[idx] == '(' and left_rem > 0) or (s[idx] == ')' and right_rem > 0):
                    dfs(idx + 1,
                            left_count,
                            right_count,
                            left_rem - (s[idx] == '('),
                            right_rem - (s[idx] == ')'), expr)

                expr.append(s[idx])

                # Simply dfs one step further if the current character is not a parenthesis.
                if s[idx] != '(' and s[idx] != ')':
                    dfs(idx + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[idx] == '(':
                    # Consider an opening bracket.
                    dfs(idx + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[idx] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    dfs(idx + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                 

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        dfs(0, 0, 0, left, right, [])     
        return ans


# - Generate all valid parentheses from string s, we can memoize them to avoid re-compute sub-problem again. It's the same idea with 140. Word Break II.
# - Then get the maximum length among those valid parentheses.
# - Filter the result by choosing parentheses which has the length **equals to** the maximum length.
class Solution_2:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        @lru_cache(None)
        def dfs(i, nOpen):
            ans = set()
            if nOpen < 0:
                return ans  # Invalid -> return 0 result
            if i == len(s):
                if nOpen == 0: ans.add("")  # Valid -> Return 1 result (empty string)
                return ans

            if s[i] == '(' or s[i] == ')':  # Case 1: Skip s[i]: '(', ')'
                ans.update(dfs(i + 1, nOpen))

            if s[i] == '(':
                nOpen += 1
            elif s[i] == ')':
                nOpen -= 1
            for suffix in dfs(i + 1, nOpen):  # Case 2: Include s[i]: '(', ')' or letter
                ans.add(s[i] + suffix)
            return ans

        validParentheses = dfs(0, 0)
        maxLen = max(map(len, validParentheses))
        return filter(lambda x: len(x) == maxLen, validParentheses)

