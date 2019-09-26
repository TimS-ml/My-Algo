# https://leetcode-cn.com/problems/super-egg-drop/
# DP
# space complexity O(KN)


class Solution:
    def superEggDrop(self, K, N):
        # 这里的dp[i]是i个蛋，能预测多少层，步数j被专门拿出来了
        dp = [0] * (K+1)
        j = 0
        while dp[K] < N:  # while用得很好
            j += 1
            for i in range(K, 0, -1):  # [1, K]
                dp[i] = dp[i-1] + dp[i] + 1
        return j


K = 2
N = 5
# K = 4
# N = 5000

print(Solution().superEggDrop(K, N))
