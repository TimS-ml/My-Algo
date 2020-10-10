'''
# Code Explain:
- Time complexity: O(n * n**0.5)
    - double loop
- Space complexity: O(n)

[1] Base State
[2] State Transfer Equation
- dp[i] = min(dp[i], dp[i-j**2]+1)
[3] Initialize Conditions
- dp[0] = 0
[4] State Compression (optional)
[5] Terminate Conditions

The candidate way is to add a perfect square number j*j to a sum of perfect square numbers that equals to i. And it can be generized as i-j*j + j*j.
So the least number of perfect square numbers that sum up to i-j*j is dp[i-j*j]. So candidate answer is dp[i-j*j]+1(add one more number j*j).

# Pros and Cons:
## Pros:

## Cons:
Using DP is really really slow in this problem

# Notation:

'''


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(i**0.5) + 1)) + 1
        return dp[n]

    def numSquares2(self, n: int) -> int:
        dp = [0] + [4] * n  # 4 sqr theorem
        for i in range(1, n + 1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i - j**2] + 1, dp[i])
                j += 1
        return dp[n]


n = 13
print(Solution().numSquares2(n))
