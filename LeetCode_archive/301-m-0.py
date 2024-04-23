'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[1] func -> count number of parentheses to remove -> return l and r
- does location matters?
- ? func check is valid

for r:
')()' -> remove only 2nd r

for l:
'()()(()' -> remove l any except 1st one

rules:
- total l == total r
- l >= r in the middle

[2] generate dfs and count removeal

'''

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(idx):
            l = r = 0
            for _ in range(idx):
                if s[idx] == '(':
                    l += 1

                elif s[idx] == ')': 
                    r += 1
            return l - r

        def helper(idx, l, r):
            balance = isValid(idx) > 0
            if balance > 0:
                if s[idx] == '(':
                    helper(idx + 1, l, r)
                    helper(idx + 1, l - 1, r)
    
            elif balance < 0:
                if s[idx] == ')': 
                    helper(idx + 1, l, r)
                    helper(idx + 1, l - 1, r)
        
        visited = set()
        ans = []
    
        return ans
