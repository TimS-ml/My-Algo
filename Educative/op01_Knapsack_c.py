'''
# Code Explain:
- Time complexity: O(N*C) 
where ‘N’ is the number of items and ‘C’ is the knapsack capacity
- Space complexity: O(N*C)

# Pros and Cons and Notation:
Bottom-up Dynamic Programming

In Bottom-to-top Dynamic Programming the approach is also based on *storing sub-solutions* in memory,
but they are solved in a different order (*from smaller to bigger*),
and the resultant general structure of the algorithm is not recursive. LCS algorithm is a classic Bottom-to-top DP example.

[1] Base State
[2] State Transfer Equation => idx from idx-1 (bottom up)
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions

=> state: maximum profit for capacity 'c' and **calculated from 0 to 'i' items (dp[i][c])**
what we want: ans = dp[len(profits)-1][capacity]: all items + input capacity
'''

def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    # same as sol b
    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    # for i in range(n):
    #     dp[i][0] = 0

    # [3] Initialize Conditions
    # if we have only one weight (one product), we will take it if it is not more than the capacity
    # only one options (choose '0' if we can)
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)
    
    # call our print function
    # print_selected_elements(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner.
    
    #  for index in range(len(dp)):
    #      print(dp[index])
    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
