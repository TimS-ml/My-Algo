'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] Return

# Pros and Cons:
## Pros:

## Cons:

# Notation:
sol4 (for simple dp)
If the current state is only related to the previous one, we can all simplify the space complexity by scrolling the array and variables

'''


class Solution:
    # simple recursion
    def climbStairs(self, n) -> int:
        if n == 1 or n == 2:
            return 1
        return climbStairs(n-1) + climbStairs(n-2)


    # Momoization
    def climbStairs2(self, n) -> int:
        cache = {}
        def climb(i, n):
            if i in cache:
                return cache[i]
            if i > n:
                return 0
            if i == n:
                return 1
            else:
                ans = climb(i + 1, n) + climb(i + 2, n)
            cache[i] = ans
            return ans
        return climb(0, n)


    def climbStairs3(self, n) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


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


print(Solution().climbStairs(5))

