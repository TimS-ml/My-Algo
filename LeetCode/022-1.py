'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/
'''


class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        dp = []
        dp.append([None])  # 0组括号时记为None
        dp.append(['()'])  # 1组括号只有一种情况
        for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):  # 开始遍历 p q , 其中p+q=i-1 , j 作为索引
                l1 = dp[j]  # p = j 时的括号组合情况
                l2 = dp[i - 1 - j]  # q = (i-1) - j 时的括号组合情况
                for k1 in l1:
                    for k2 in l2:
                        if k1 == None:
                            k1 = ''
                        if k2 == None:
                            k2 = ''
                        el = '(' + k1 + ')' + k2
                        l.append(el)  # 把所有可能的情况添加到 l 中
            dp.append(l)  # l这个list就是i组括号的所有情况, 添加到dp中, 继续求解i=i+1的情况
        return dp[n]

    # same...
    def generateParenthesis_2(self, n: int):
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            for p in range(i):
                l1 = dp[p]
                l2 = dp[i - 1 - p]
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append('({0}){1}'.format(k1, k2))

        return dp[n]
