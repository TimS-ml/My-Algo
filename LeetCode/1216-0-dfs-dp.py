'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from functools import lru_cache

class Solution:
    # DFS
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def helper(i, j, remaining):
            if remaining == -1:
                return False
            if j-i+1 <= 1:  # if length is <= 1
                return True
            if (i, j, remaining) in memo:
                return memo[(i, j, remaining)]
            
            if s[i] == s[j]:
                memo[(i, j, remaining)] = helper(i+1, j-1, remaining)
            else:
                memo[(i, j, remaining)] = helper(i+1, j, remaining-1) or helper(i, j-1, remaining-1)
            return memo[(i, j, remaining)]
        
        memo = {}
        return helper(0, len(s)-1, k)

    # a better DFS
    # a while loop inside helper will reduce the call of recursion thus increase the speed
    def isValidPalindrome_2(self, s: str, k: int) -> bool:
        if s == s[::-1]: return True
        
        @lru_cache(None)
        def helper(l, r, numOfChoices):
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    if numOfChoices < k:
                        return helper(l+1, r, numOfChoices+1) or helper(l, r-1, numOfChoices+1)
                    elif numOfChoices == k:  # cannot afford more mistakes
                        return False
            return True
        
        return helper(0, len(s)-1, 0)

    # DP
    # i, j: left and right pointers
    def isValidPalindrome_dp(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]  # add additional 0
        for i in range(n + 1): 
            for j in range(n + 1): 
                if not i or not j: 
                    dp[i][j] = i or j 
                elif s[i - 1] == s[n - j]: 
                    dp[i][j] = dp[i - 1][j - 1] 
                else: 
                    # 1 del
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n] <= k * 2
