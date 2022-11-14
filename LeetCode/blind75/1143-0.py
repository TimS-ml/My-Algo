'''
case:
t1 xxaxxa
t2 yya

s1[i] == s2[j] case

match1
xxaxxa <- i
yya <- j
dp[3][3] = 1

match2
xxaxxa <- i
   yya <- j

dp[6][3] = 1


case: 
t1 acabc
t2 abc

       a  b  c
  [[0, 0, 0, 0],
a  [0, 1, 1, 1],
c  [0, 1, 1, 2],
a  [0, 1, 1, 2],
b  [0, 1, 2, 2],
c  [0, 1, 2, 3]]
'''

class Solution:
    def longestCommonSubsequence(self, str1, str2) -> int:
        m, n = len(str1), len(str2)

        # m='', n=xxx, dp=0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
