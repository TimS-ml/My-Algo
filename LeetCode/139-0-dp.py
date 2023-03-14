'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

"dogs"
["dog","s","gs"]
'''

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for w in wordDict:
                if i >= len(w):  # this will cut some branchs
                    if w == s[i-len(w):i]:
                        dp[i] = dp[i-len(w)]
                if dp[i]:  # once find one possible dp[i] combo, stop searching 
                    break
        return dp[-1]

    def wordBreak_2(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

    # dp, should pad a dp[0]
    # def wordBreak_3(self, s: str, wordDict: List[str]) -> bool:
    #     dp = [False] * len(s)
    #     for i in range(len(s)):
    #         for w in wordDict:
    #             j = i - len(w)
    #             if w == s[j + 1:i + 1] and (dp[j] or j == -1):
    #                 dp[i] = True
    #     return dp[-1]



# False
s = "catsandog"
w = ["cats", "dog", "sand", "and", "cat"]

# True
s = "catsandog"
w = ["cats", "og", "sand", "and", "cat"]

# # True
# s = "applepenapple"
# w = ["apple", "pen"]

# # True
# s = "appenapp"
# w = ["ap", "pen", "app"]

print(Solution().wordBreak(s, w))
