'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

leading 0?
    0

- 1 dig or (2 dig + < 26)
- bf: for loops

- dfs with cache (hash)

Feedback
- Fully understand the cases (60, 909)
    - Clear the edge case (dfs terminate cases)
- Go over at least 1-2 cases
    - so that you will realize ans is not mul, is add
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        self.comb = 0
        def dfs(comb, arr):
            if len(arr) == 2 and int(arr) < 26:
                return 2 * self.comb
            else:
                return 1 * self.comb
            dfs(comb, arr[1:])
            dfs(comb, arr[2:])
        dfs(0, s)
        return self.comb
