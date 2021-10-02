'''
# Code Explain:
- Time complexity: O(l1 * l2)
- Space complexity: O(l1 * l2)

# Pros and Cons and Notation:

this solution can be further compressed!

dp

state: 
dp[i][j] = if s1[i] and s2[j] can make s3[i+j]

transfer:
For s1
if s3[i+j] == s1[i], and dp[i-1][j] == 1:
    dp[i][j] == 1

init:
dp[0][0] = 1
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True

        for i in range(1, l1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for j in range(1, l2 + 1):
            dp[0][j] = (dp[0][j - 1] and s2[j - 1] == s3[j - 1])
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                           (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]

    def isInterleave_2(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = True

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i - 1][j]
                                            and s1[i - 1] == s3[i + j - 1])
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j - 1]
                                            and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


s1 = "aabcce"
s2 = "dbbca"
s3 = "aadbbcbcace"
print(Solution().isInterleave_2(s1, s2, s3))
