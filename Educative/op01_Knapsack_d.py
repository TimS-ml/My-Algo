# op01_c with O(C) space complexity


def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    # we only need one previous row to find the optimal solution, overall we need '2' rows
    # the above solution is similar to the previous solution, the only difference is that
    # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
    dp = [[0 for x in range(capacity + 1)] for y in range(2)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(0, capacity + 1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
            # exclude the item
            profit2 = dp[(i - 1) % 2][c]
            # take maximum
            dp[i % 2][c] = max(profit1, profit2)

    return dp[(n - 1) % 2][capacity]


def solve_knapsack_v2(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [0 for x in range(capacity + 1)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]
            # exclude the item
            profit2 = dp[c]
            # take maximum
            dp[c] = max(profit1, profit2)

    return dp[capacity]


def main():
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
