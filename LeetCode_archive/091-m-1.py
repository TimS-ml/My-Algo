class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]


# Wrong: dealing with 0
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s[0] == '0':
#             return 0

#         s = [int(c) for c in s]
#         # print(s)
#         dp = [0] * (len(s) + 1)
#         dp[0] = 1
#         dp[1] = 1

#         for i in range(2, len(s)+1):
#             print(s[i-1])
#             # treat as 12 or 1, 2
#             if s[i-1] != 0:
#                 if s[i-2] == 0:
#                     dp[i] = dp[i-2]
#                 else:
#                     dp[i] = dp[i-1] + dp[i-2]
#             else:
#                 dp[i] = dp[i-2]

#         return dp[-1]
