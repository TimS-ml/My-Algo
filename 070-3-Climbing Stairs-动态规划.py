# https://leetcode-cn.com/problems/climbing-stairs/

# https://www.zhihu.com/question/23995189
# https://blog.csdn.net/tyhj_sf/article/details/53969072
# 如果问题是由【交叠】的子问题所构成，我们就可以用动态规划技术来解决它
# 子问题会有重叠，一个子问题在求解后，可能会再次求解
# 所以需要记录子问题的计算结果
# 动态规划也是空间换时间的

# 实际上方法3和2的区别在于一个是从上往下一个是从下往上


class Solution:
    def climbStairs(self, n) -> int:
        if n == 1:
            return 1
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        # print(memo)  # [0, 1, 2, 3, 5, 8]
        return memo[n]


print(Solution().climbStairs(5))
