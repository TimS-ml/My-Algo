'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # this is wrong, it's a 1d array
        # dp = [[1] for _ in range(n) for _ in range(m)]
        dp = [[1] * n for row in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]

    # notice that: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # which means we can do rolling, compress row for example
    # compress inner loop is easier
    def uniquePaths_2(self, m: int, n: int) -> int:
        currI = [1 for _ in range(m)]
        prevI = [1 for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                currI[j] = prevI[j] + currI[j - 1]
            prevI = currI[:]  # !!! 
        return prevI[-1]

