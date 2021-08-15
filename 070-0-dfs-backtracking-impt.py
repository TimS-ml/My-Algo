'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:
(tree) top-down: bigger problem first
    return c[n] => c[n-1] ...
                => c[n-2] ...

(tree) bottom-up: smaller problem first
    start with dp[1] and dp[2]
        dp[3] = dp[1] + dp[2] ...

sol4 (for simple dp)
If the current state is only related to the previous one, we can all simplify the space complexity by scrolling the array and variables
'''


class Solution:
    # simple recursion
    # brute force
    # top-down
    def climbStairs(self, n) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # dfs: recursion + cache
    # top-down
    def climbStairs_2(self, n) -> int:
        cache = [None for _ in range(n)]

        def climb(i):
            # we assume stair # start with 0, not 1
            if i == 0 or i == 1:
                return i + 1
            if cache[i]:
                return cache[i]
            else:
                cache[i] = climb(i - 1) + climb(i - 2)
            # print(cache)
            return cache[i]

        return climb(n - 1)

    # dfs: use dict as cache + different way of return
    def climbStairs_2_v2(self, n) -> int:
        cache = {}

        def climb(i):
            if i in cache:
                return cache[i]
            if i > n:
                return 0
            if i == n:
                return 1
            else:
                cache[i] = climb(i + 1) + climb(i + 2)
            return cache[i]

        return climb(0)

class Solution_backtrack:
    # backtrack: go over all the routines
    def climbStairs(self, n):
        def backtrack(subset):
            if n == sum(subset):
                ans.append(subset[:])
                return
            for i in range(1, 2+1):  # 1 step or 2 steps
                if n - sum(subset) - i >= 0:
                    subset.append(i)
                    backtrack(subset)
                    # reverse movement
                    subset.pop()

        ans = []
        backtrack([])
        return ans

    # backtrack: go over all the routines
    def climbStairs_2(self, n):
        def backtrack(subset, target_sum):
            if target_sum == 0:
                ans.append(subset[:])
                return
            for i in range(1, 2+1):  # 1 step or 2 steps
                if target_sum - i >= 0:
                    subset.append(i)
                    backtrack(subset, n - sum(subset))
                    # reverse movement
                    subset.pop()

        ans = []
        backtrack([], n)
        return ans



# backtrack solution
result = Solution_backtrack().climbStairs_2(5)
print(len(result))
print(result)

# non-backtrack solution
# print(Solution().climbStairs_2_v2(5))
