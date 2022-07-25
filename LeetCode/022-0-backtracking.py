'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

for backtracking: path and search space
'''


class Solution:
    def generateParenthesis(self, n: int):
        def backtrack(subStr, left, right):
            # or use if right == n
            if len(subStr) == 2 * n:
                ans.append(subStr)
                return
            # if left < n and if right < left will keep balance
            if left < n:
                backtrack(subStr + '(', left + 1, right)
            if right < left:
                backtrack(subStr + ')', left, right + 1)

        ans = []
        backtrack('', 0, 0)
        return ans

    # same... but we need to check if left is 0
    # otherwise will include '()()(('
    def generateParenthesis_2(self, n: int):
        def backtrack(left, subPath):
            if len(subPath) == 2 * n:
                if left == 0:
                    ans.append(''.join(subPath))
                # ans.append(''.join(subPath))
                return

            if left < n:
                subPath.append('(')
                backtrack(left + 1, subPath)
                subPath.pop()  # len(subPath) == 2*n and left != 0
            if left > 0:
                subPath.append(')')
                backtrack(left - 1, subPath)
                subPath.pop()

        ans = []
        backtrack(0, [])
        return ans

    def generateParenthesis_dp(self, n: int):
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

print(Solution().generateParenthesis(3))
# print(Solution().generateParenthesis_2(3))
