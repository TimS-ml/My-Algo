# "dogs"
# ["dog","s","gs"]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(dp)):
            for w in wordDict:
                if i >= len(w):
                    if w == s[i-len(w):i]:
                        dp[i] = dp[i-len(w)]
                if dp[i]:
                    break
        return dp[-1]

    # a better way of writting
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
