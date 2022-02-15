'''
# Code Explain:
- Time complexity: O(mn)
- Space complexity: O(mn)


Tricky part:
- Operation position does not affect result
    - so we do all the position at the end of string

Let's simplify the question first
- insert A <=> delete B, so operations are:
    - insert A
    - insert B
    - replace A
- dp state is distance
    - from A to '', distance=len(A)
- dp dim is 2 (A and B)
    - dp[i][j] is distance between A[:i] and B[:j]

- when word1[i] == word2[j]
    - dp[i][j] = dp[i-1][j-1]
- when word1[i] != word2[j]
    - dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

- insert A   dp[i-1][j]
- insert B   dp[i][j-1]
- replace A  dp[i][j]
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # has at lease one empty string
        if n * m == 0:
            return n + m

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # init
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)

        return dp[n][m]
