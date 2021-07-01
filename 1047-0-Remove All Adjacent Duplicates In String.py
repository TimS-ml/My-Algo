'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

- How to remove duplicate chars?
    - copy of string or pop
- Recursion?

'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                # do sth
                continue
