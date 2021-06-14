'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ 
The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don’t have multiple quantities of any item.

# Code Explain:
- Time complexity: O(2^N)
- Space complexity: O(N)

# Pros and Cons and Notation:

Brute-force, Overlapping Sub-problems
[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] Terminate Conditions
'''

def solve_knapsack(profits, weights, capacity):
    # [3] Initialize Conditions
    return knapsack_recursive(profits, weights, capacity, 0)


# this capacity is more like 'capacity left' for current options
def knapsack_recursive(profits, weights, capacity, currentIndex):
    # [4] Terminate Conditions
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this

    # [2.1] State Transfer Equation with current item
    # capacity - weights[currentIndex] >= 0, capacity change after include item[currentIndex]
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + \
                    knapsack_recursive(
                        profits, 
                        weights, 
                        capacity - weights[currentIndex],  # this is different
                        currentIndex + 1)

    # [2.2] State Transfer Equation without current item
    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(
                profits, 
                weights, 
                capacity, 
                currentIndex + 1)

    return max(profit1, profit2)


def main():
    # profits, weights, capacity
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
