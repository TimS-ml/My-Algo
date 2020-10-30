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

    # recursion + cache
    # top-down
    def climbStairs2(self, n) -> int:
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

    def climbStairs2_(self, n) -> int:
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

    # Momoization
    # bottom-up
    def climbStairs3(self, n) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # Momoization + Scrolling
    # Scrolling to reduce space complexity
    def climbStairs4(self, n) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second


print(Solution().climbStairs2(5))
