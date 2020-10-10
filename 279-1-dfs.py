'''
# Code Explain:
- Time complexity: O(n * n**0.5) ???
- Space complexity: O()

Output from sol1
0 [] 13 inf
0 [9] 4 inf
0 [9, 9] -5 inf
1 [9, 4] 0 inf  <- update ans
2 [9, 1] 3 2
1 [4] 9 2
1 [4, 4] 5 2
2 [4, 1] 8 2
2 [1] 12 2
2 [1, 1] 11 2

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    def numSquares(self, n: int) -> int:
        # Generate the squares, reverse to be in decreasing order for efficiency.
        sqrs = [i**2 for i in range(1, int(n**0.5) + 1)][::-1]
        ans = float('inf')

        def dfs(start, subset, number):
            nonlocal ans
            print(start, subset, number, ans)
            # If the current subset we're using >= the min that lead to the target return.
            # If number < 0 or > n return.
            if len(subset) >= ans or number < 0:
                return
            # when len(subset) < ans.
            elif number == 0:
                ans = len(subset)
                return
            else:
                for i in range(start, len(sqrs)):
                    # after: subset + [sqrs[i]], len increase 1
                    # backtrack, same as append->dfs->pop
                    dfs(i, subset + [sqrs[i]], number - sqrs[i])

        dfs(0, [], n)
        return ans if ans != float('inf') else -1


n = 13
print(Solution().numSquares(n))
