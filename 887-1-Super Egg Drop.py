# https://leetcode-cn.com/problems/super-egg-drop/
# 暴力法
# time complexity
# space complexity


class Solution:
    def superEggDrop(self, K, N):
        def recursive(K, N):
            if(K == 1 or N == 0 or N == 1):
                return N

            minimun = N
            i = 1
            while i <= N:
                # tMin判断i在F上or下（因为并没有给出F）
                # 输出的minimum number of moves是任意F的
                # F取特定值的时候恰巧可以少一两步推算出来，要舍弃，所以tMin取max
                # print(i, minimun, 'recursive(%d, %d), recursive(%d, %d)' %(K-1, i-1, K, N-1))
                tMin = max(recursive(K - 1, i - 1),
                           recursive(K, N - i))  # 每次比较都要重新算一遍
                minimun = min(minimun, 1 + tMin)
                i += 1
                # print('====')
            return minimun

        return recursive(K, N)


K = 2
N = 5
# K = 3
# N = 25

print(Solution().superEggDrop(K, N))

# 1 5 recursive(1, 0), recursive(2, 4)
# 1 4 recursive(1, 0), recursive(2, 3)
# 1 3 recursive(1, 0), recursive(2, 2)
# 1 2 recursive(1, 0), recursive(2, 1)
# ====
# 2 2 recursive(1, 1), recursive(2, 1)
# ====
# ====
# 2 3 recursive(1, 1), recursive(2, 2)
# ====
# 3 2 recursive(1, 2), recursive(2, 2)
# ====
# ====
# 2 3 recursive(1, 1), recursive(2, 3)
# 1 2 recursive(1, 0), recursive(2, 1)
# ====
# 2 2 recursive(1, 1), recursive(2, 1)
# ====
# ====
# 3 3 recursive(1, 2), recursive(2, 3)
# ====
# 4 3 recursive(1, 3), recursive(2, 3)
# ====
# ====
# 2 4 recursive(1, 1), recursive(2, 4)
# 1 3 recursive(1, 0), recursive(2, 2)
# 1 2 recursive(1, 0), recursive(2, 1)
# ====
# 2 2 recursive(1, 1), recursive(2, 1)
# ====
# ====
# 2 3 recursive(1, 1), recursive(2, 2)
# ====
# 3 2 recursive(1, 2), recursive(2, 2)
# ====
# ====
# 3 3 recursive(1, 2), recursive(2, 4)
# 1 2 recursive(1, 0), recursive(2, 1)
# ====
# 2 2 recursive(1, 1), recursive(2, 1)
# ====
# ====
# 4 3 recursive(1, 3), recursive(2, 4)
# ====
# 5 3 recursive(1, 4), recursive(2, 4)
# ====
# 3
