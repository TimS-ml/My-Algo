# https://leetcode-cn.com/problems/super-egg-drop/
# DP
# time complexity O(KN)
# space complexity O(KN)


class Solution:
    def superEggDrop(self, K, N):
        # int[][] dp = new int[K + 1][N + 1];
        # 这里的dp[i][j]是i个蛋, j步, 能预测多少层
        dp = [[0 for col in range(N + 1)] for row in range(K + 1)]

        for j in range(1, N + 1):  # number of move(s)
            dp[0][j] = 0  # zero egg
            for i in range(1, K + 1):  # number of egg(s)
                # 本次扔之后可能测出来的层数 + 本次扔之前已经测出来的层数
                # 鸡蛋碎了, 少了一个蛋, 少了一步, dp[i-1][j-1] + 1
                #   第x层和第x~N层都大于F
                # 鸡蛋没碎, , 少了一步, dp[i][j-1]
                #   第0~x层小于F
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] + 1
                if dp[i][j] >= N:
                    return j

        return i


K = 2
N = 5
# K = 4
# N = 5000

print(Solution().superEggDrop(K, N))
