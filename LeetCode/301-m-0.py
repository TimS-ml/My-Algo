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
