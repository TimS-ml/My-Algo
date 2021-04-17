# Brute-force, Overlapping Sub-problems
# [1] Base State
# [2] State Transfer Equation
# [3] Initialize Conditions
# [4] Terminate Conditions

# time : O(2^n)
# space: O(n)

def solve_knapsack(profits, weights, capacity):
    # [3] Initialize Conditions
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, currentIndex):
    # [4] Terminate Conditions
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this

    # [2.1] State Transfer Equation
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            profits, 
            weights, 
            capacity - weights[currentIndex],
            currentIndex + 1)

    # [2.2] State Transfer Equation
    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)


def main():
    # profits, weights, capacity
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
