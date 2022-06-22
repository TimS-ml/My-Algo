'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ 
The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don’t have multiple quantities of any item.

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
    # you have to avoid to init to 0, since you need to return 0 in top-down
    cache = [[-1] * (capacity + 1) for _ in range(len(profits))]
    L = len(profits)
    
    # idx is from top to bottom
    def dfs(idx, c):
        if c <= 0 or idx >= L:
            return 0
        if cache[idx][c] != -1:
            return cache[idx][c]
        p1, p2 = 0, 0
        if weights[idx] <= c:
            # this is +1
            p1 = profits[idx] + dfs(idx + 1, c - weights[idx])
        p2 = dfs(idx + 1, c)
        cache[idx][c] = max(p1, p2)
        return cache[idx][c]

    return dfs(0, capacity)


def main():
    # profits, weights, capacity
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
