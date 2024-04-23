'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

check 1541
ans represents the number of left/right parentheses already added.
    in this question, only for left parentheses
right represents the number of right parentheses needed.
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = right = 0
        for c in s:
            right += 1 if c == '(' else -1
            # It is guaranteed right >= -1
            if right == -1:
                ans += 1
                right += 1  # reset to 0
        return ans + right
