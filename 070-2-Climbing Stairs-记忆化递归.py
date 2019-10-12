# https://leetcode-cn.com/problems/climbing-stairs/
# 把每一步的结果存储在 memo 数组之中
# 每当函数再次被调用，我们就直接从 memo 数组返回结果


class Solution:
    def climb(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = Solution().climb(i+1, n, memo) + \
            Solution().climb(i+2, n, memo)
        print(i, n, memo)
        return memo[i]

    def climbStairs(self, n) -> int:
        memo = [0] * n
        return Solution().climb(0, n, memo)


print(Solution().climbStairs(5))

# 比如算memo[3]的时候会用到memo[4]和memo[5]，总之省下了一些重复计算的
# 直到最后一步memo[0] = 8
# 0 5 [0, 0, 0, 0, 0]
# 1 5 [0, 0, 0, 0, 0]
# 2 5 [0, 0, 0, 0, 0]
# 3 5 [0, 0, 0, 0, 0]
# 4 5 [0, 0, 0, 0, 0]
# 4 5 [0, 0, 0, 0, 1]
# 3 5 [0, 0, 0, 2, 1]
# 2 5 [0, 0, 3, 2, 1]
# 1 5 [0, 5, 3, 2, 1]
# 0 5 [8, 5, 3, 2, 1]
