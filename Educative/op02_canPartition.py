'''
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# Code Explain:
- Time complexity: O(2^N)
- Space complexity: O(N)

# Pros and Cons and Notation:
important: 
- the two subsets have the sum of sum(num)/2
- you only need to find one subset that sum(subset) = sum(num)/2

basic solution
for each number 'i' 
  create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively 
      process the remaining numbers
  create a new set WITHOUT number 'i', and recursively process the remaining items 
return true if any of the above sets has a sum equal to 'S/2', otherwise return false

Brute-force, Overlapping Sub-problems
[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] Terminate Conditions
'''


def can_partition(num):
    s = sum(num)
    # if 's' is a an odd number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    # [3] Initialize Conditions
    return can_partition_recursive(num, s / 2, 0)


# 'num' is unchange in this function, same as profits, weights in op01
# 'sum' same as capacity in op01
def can_partition_recursive(num, sum, currentIndex):
    # [4] Terminate Conditions
    if sum == 0:
        return True

    n = len(num)
    if n == 0 or currentIndex >= n:
        return False

    # [2.1] State Transfer Equation
    # recursive call after choosing the number at the `currentIndex`
    # if the number at `currentIndex` exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
        if (can_partition_recursive(num, 
                                    sum - num[currentIndex],
                                    currentIndex + 1)):
            return True

    # [2.2] State Transfer Equation
    # recursive call after excluding the number at the 'currentIndex'
    return can_partition_recursive(num, 
                                   sum, 
                                   currentIndex + 1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))  # [1,3,4] and [1,7]
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
