class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        dp = [[0] * len(s) for _ in range(len(s))]

        # init: filling out the diagonal by 1
        # single char is True
        for i in range(len(s)):
            dp[i][i] = 1
            ans += 1

        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
                    dp[i][j] = 1
                    ans += 1

        return ans
