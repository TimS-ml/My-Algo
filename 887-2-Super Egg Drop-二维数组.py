# https://leetcode-cn.com/problems/super-egg-drop/
# https://vimsky.com/article/790.html
# 空间换时间
# time complexity O(KN^2)
# space complexity O(KN)


class Solution:
    def superEggDrop(self, K, N):
        # int[][] midResults = new int[K + 1][N + 1];
        # 这里的midResults[i][j]是i个蛋，j层，需要多少步
        midResults = [[0 for col in range(N+1)] for row in range(K+1)]
        
        for i in range(1, K+1):
            midResults[i][0] = 0  # zero floor

        for j in range(1, N+1):
            midResults[1][j] = j  # only one egg
            midResults[0][j] = 0  # no egg

        print(midResults)

        for k in range(2, K+1):  # start from 2 eggs，已经有了1 egg的数据
            for j in range(1, N+1):
                minimun = N
                for x in range(1, j+1):
                    tMin = max(midResults[k-1][x-1], midResults[k][j-x])
                    minimun = min(minimun, 1 + tMin)
                midResults[k][j] = minimun
        
        print(midResults)
        return midResults[K][N]


K = 2
N = 5
# K = 4
# N = 5000

print(Solution().superEggDrop(K, N))
