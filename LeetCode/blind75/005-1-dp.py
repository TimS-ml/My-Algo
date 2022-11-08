'''
dp[r][c] = the row and col in the dp table represent the slicing index on the string s (inclusive)
'''

class Solution:
    def longestPalindrome(self, s):
        ans = ''
        dp = [[0] * len(s) for _ in range(len(s))]

        # init: filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            ans = s[i]

        # filling the dp table
        for i in range(len(s) - 1, -1, -1):
            # j starts from the i location : to only work on the upper side of the diagonal
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True
                    # if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence
                        if len(ans) < len(s[i:j + 1]):
                            ans = s[i:j + 1]

        return ans

