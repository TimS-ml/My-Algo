'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

for dp:
[1] Base State
dp[i]: if s[:i] is valid (T/F)

[2] State Transfer Equation
for 0 < j < i and dp[j] is True
dp[i] = (dp[j] && check(s[j:i-1]))

[3] Initialize Conditions
dp[0] = True

[4] State Compression (optional)

[5] Terminate Conditions


- Time complexity: O(n^2)
- Space complexity: O(n^2)

for backtrack:
[1] Base State
func backtrack(substr)

[2] State Transfer Equation
func backtrack(substr[i:])

[3] Backtrack senario

[4] Initialize Conditions
init ans = False
if substr == 0 -> return True

[5] Terminate Conditions


# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List
import functools


class Solution:
    # dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                # [1] i == len(w) or [2] dp[j] == True
                j = i - len(w)
                if w == s[j + 1:i + 1] and (dp[j] or j == -1):
                    dp[i] = True
        return dp[-1]

    # or if you preferred this way
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                # [1] i == len(w) or [2] dp[j] == True
                j = i - len(w)
                if w == s[j + 1:i + 1] and (dp[j] or j == -1):
                    dp[i] = True
        return dp[-1]

    # backtrack
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        @functools.lru_cache(None)
        def backtrack(substr):
            if(not substr):
                return True
            res=False
            for i in range(1,len(substr)+1):
                if(substr[:i] in wordDict):
                    res=backtrack(substr[i:]) or res
            return res
        return backtrack(s)


# # False
# s = "catsandog"
# w = ["cats", "dog", "sand", "and", "cat"]

# # True
# s = "applepenapple"
# w = ["apple", "pen"]

# True
s = "appenapp"
w = ["ap", "pen", "app"]

print(Solution().wordBreak(s, w))
