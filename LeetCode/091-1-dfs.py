'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def dfs(idx):
            # Out of boundary
            if idx == len(s):
                return 1

            # Last digit and not 0
            if idx == len(s)-1 and s[idx] != '0':
                return 1

            # If the string starts with a zero, it can't be decoded
            if s[idx] == '0':
                return 0

            # 1 dig
            ans = dfs(idx + 1)

            # 2 digs
            if int(s[idx : idx + 2]) <= 26:
                ans += dfs(idx + 2)

            return ans

        return dfs(0)
