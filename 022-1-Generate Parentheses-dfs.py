# https://leetcode-cn.com/problems/generate-parentheses/
# left==0相当于左右括号的平衡


class Solution:
    def generateParenthesis(self, n: int):
        def dfs(left, path, res, n):
            if len(path) == 2 * n:
                if left == 0:
                    res.append("".join(path))
                return

            if left < n:
                path.append("(")
                # print('left < n', left+1, path, res)
                dfs(left+1, path, res, n)
                path.pop()  # len(path) == 2*n and left != 0

            if left > 0:
                path.append(")")
                # print('left > 0', left-1, path, res)
                dfs(left-1, path, res, n)
                path.pop()

        res = []
        dfs(0, [], res, n)
        return res


print(Solution().generateParenthesis(3))
