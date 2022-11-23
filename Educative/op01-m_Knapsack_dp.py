'''
Given the weights and profits of 'N' items, we are asked to put these items in a knapsack with a capacity 'C.'
The goal is to get the maximum profit out of the knapsack items.
Each item can only be selected once, as we don't have multiple quantities of any item.

# Code Explain:
- Time complexity: O(N * C)
- Space complexity: O(N * C)



[1] Base State
dp[i][j] = maximum profit considering product 0~i, weight remain (or sum weight) is j

[2] State Transfer Equation
dp[i][j] = max(choose, not choose)

choose (at lease j-w[i] to carry product i)
dp[i][j] = p[i] + dp[i-1][j-w[i]]

not choose
dp[i][j] = dp[i-1][j]

[3] Initialize Conditions
dp[0][~] = if w[i] < c
return dp[-1][w]

[4] State Compression (optional)

[5] Terminate Conditions
w should > 0
'''


def solve_knapsack(profits, weights, capacity):
    # N * C
    # you have to init to 0, not sth else
    dp = [[-1] * (capacity + 1) for _ in range(len(profits))]

    for i in range(len(profits)):
        dp[i][0] = 0

    for c in range(capacity):
        if weights[0] <= c + 1:
            dp[0][c + 1] = profits[0]

    for i in range(1, len(profits)):
        for c in range(capacity):
            p1, p2 = 0, 0
            if weights[i] <= c + 1:
                p1 = profits[i] + dp[i - 1][c - weights[i] + 1]

            p2 = dp[i - 1][c + 1]
            dp[i][c + 1] = max(p1, p2)

    for index in range(len(dp)):
        print(dp[index])
    # print(dp)
    return dp[-1][capacity]


def main():
    # profits, weights, capacity
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
