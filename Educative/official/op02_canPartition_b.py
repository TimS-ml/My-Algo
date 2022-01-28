'''
# Code Explain:
- Time complexity: O(N * S)
- Space complexity: O(N * S)
The algorithm has the time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.

# Pros and Cons and Notation:

Top-down Dynamic Programming with Memoization
'''


def can_partition(num):
    s = sum(num)

    # if 's' is a an odd number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for _ in range(int(s / 2) + 1)] for _ in range(len(num))]
    return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 \
                else False


def can_partition_recursive(dp, num, sum, currentIndex):
    # base check
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # if we have not already processed a similar problem
    if dp[currentIndex][sum] == -1:
        # recursive call after choosing the number at the currentIndex
        # if the number at currentIndex exceeds the sum, we shouldn't process this
        if num[currentIndex] <= sum:
            if can_partition_recursive(dp, num, 
                                       sum - num[currentIndex],
                                       currentIndex + 1) == 1:
                dp[currentIndex][sum] = 1
                return 1

        # recursive call after excluding the number at the currentIndex
        dp[currentIndex][sum] = can_partition_recursive(
                                    dp, num, sum, currentIndex + 1)

    return dp[currentIndex][sum]


def main():
    print(str(can_partition([1, 2, 3, 4])))
    print(str(can_partition([1, 1, 3, 4, 7])))  # [1,3,4] and [1,7]
    print(str(can_partition([2, 3, 4, 6])))


main()
