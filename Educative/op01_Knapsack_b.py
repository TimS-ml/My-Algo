'''
# Code Explain:
- Time complexity: O(N*C) 
where ‘N’ is the number of items and ‘C’ is the knapsack capacity
- Space complexity: O(N*C + N)

# Pros and Cons and Notation:

Top-down Dynamic Programming with Memoization
Top-to-bottom Dynamic Programming is nothing else than ordinary recursion, enhanced with *memorizing the solutions for intermediate sub-problems*.

[1] Base State
[2] State Transfer Equation => idx from idx+1 (top down)
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions
'''

def solve_knapsack(profits, weights, capacity):
    # [3] Initialize Conditions
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    # [5] Terminate Conditions
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # [4] State Compression (optional)
    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    # [2.1] State Transfer Equation
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            dp, profits, weights, capacity - weights[currentIndex],
            currentIndex + 1)

    # [2.2] State Transfer Equation
    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(dp, profits, weights, capacity,
                                 currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
