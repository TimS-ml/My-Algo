'''
dp[r][c] = the row and col in the dp table represent the slicing index on the string s (inclusive)

- You go to the left bottom corner and check if it is True
- Left bottom corrner represent the inner sub_string of the current_sub_string
    - Eg. if dp[i][j]= cur_sub_string = 'ababa' --> True because dp[i+1][j-1] is True
        dp[i+1][j-1] = 'bab' = True
- Howerver if dp[i][j]= cur_sub_string = 'abaca' --> False because dp[i+1][j-1] is False
    - dp[i+1][j-1] = 'bac' = False --> not palindrom
'''


class Solution:

    def longestPalindrome(self, s):
        ans = s[0]
        dp = [[0] * len(s) for _ in range(len(s))]

        # init: filling out the diagonal by 1
        # single char is True
        for i in range(len(s)):
            dp[i][i] = 1

        '''
        For those who are still wondering why the loop is reversed and j>i:
        Consider at i==1 and j==5 and this range is palindrome if str[1] == str[5] and i==2 and j==4 is palindrome.
        You see we have to compute 2,4 before 1,5 and that's the reason we start from the bottom to compute 2,4 first
        In other words, calc i in desc order OR calc j in asc order
        '''

        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                # if it's a two char string or if the remaining string is a palindrome too
                if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
                    dp[i][j] = 1
                    # we also need to keep track of the maximum palindrom sequence
                    if len(ans) < len(s[i:j + 1]):
                        ans = s[i:j + 1]

        # for j in range(len(s)):
        #     for i in range(j):
        #         if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
        #             dp[i][j] = 1
        #             if j - i + 1 > len(ans):
        #                 ans = s[i:j + 1]

        return ans
