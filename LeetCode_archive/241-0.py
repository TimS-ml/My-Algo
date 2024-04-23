'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution(object):

    def diffWaysToCompute(self, expression):
        memo = {}
        ops = {
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
        }

        def dfs(ex):
            if ex in memo:
                return memo[ex]
            if ex.isnumeric():
                return [int(ex)]
            ans = []
            for i, c in enumerate(ex):
                if c in "+-*":
                    left = dfs(ex[:i])
                    right = dfs(ex[i + 1:])
                    # print(left, right)
                    ans += [ops[c](l, r) for l in left for r in right]
                    # ans += list(
                    #     eval(str(l) + c + str(r)) for l in left for r in right)
            memo[ex] = ans
            return ans

        return dfs(expression)


e = "2-1-1"
print(Solution().diffWaysToCompute(e))
