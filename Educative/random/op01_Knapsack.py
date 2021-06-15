'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ 
The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don’t have multiple quantities of any item.

# Code Explain:
- Time complexity: O(2^N)
- Space complexity: O(N)

# Pros and Cons and Notation:

Top down
[1] Base State
[2] State Transfer Equation => idx from idx+1 (top down)
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions
'''


def solve_knapsack(profits, weights, capacity):
    # capacity should include 0
    cache = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    def top_down_dp(cache, idx, curr_capacity):
        # I don't think curr_capacity would <0
        if curr_capacity <= 0 or idx >= len(profits):
            return 0

        if cache[idx][curr_capacity] != -1:
            return cache[idx][curr_capacity]

        p1 = 0
        if weights[idx] <= curr_capacity:
            p1 = profits[idx] + \
                top_down_dp(cache, idx+1,
                            curr_capacity-weights[idx])

        p2 = top_down_dp(cache, idx + 1, curr_capacity)

        return max(p1, p2)

    return top_down_dp(cache, 0, capacity)


def main():
    # profits, weights, capacity
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
