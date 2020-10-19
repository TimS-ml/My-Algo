'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

[1] Base State
dp[i]: if s[:i] is valid (T/F)

[2] State Transfer Equation
for 0 < j < i and dp[j] is True
dp[i] = (dp[j] && check(s[j:i-1]))

[3] Initialize Conditions
dp[0] = True

[4] State Compression (optional)

[5] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                # [1] i == len(w) or [2] dp[j] == True
                j = i - len(w)
                if w == s[j + 1:i + 1] and (dp[j] or j == -1):
                    dp[i] = True
        return dp[-1]


# # False
# s = "catsandog"
# w = ["cats", "dog", "sand", "and", "cat"]

# True
s = "applepenapple"
w = ["apple", "pen"]

print(Solution().wordBreak(s, w))
