'''
# Code Explain:
- Time complexity: O(N * S)
- Space complexity: O(N * S)
The algorithm has the time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.

# Pros and Cons and Notation:

Bottom-up Dynamic Programming
dp[i][s] will be ‘true’ if we can make the sum ‘s’ from the first ‘i’ numbers
'''


def can_partition(num):
    s = sum(num)

    # if 's' is a an odd number, we can't have two subsets with same total
    if s % 2 != 0:
        return False

    n = len(num)
    # the range is quite different from op02_b
    dp = [[False for _ in range(int(s / 2) + 1)] for _ in range(n)]

    # init
    # populate the s=0 columns, as we can always for '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, int(s / 2) + 1):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s / 2) + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            # else if we can find a subset to get the remaining sum
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    # the bottom-right corner will have our answer.
    return dp[n - 1][int(s / 2)]


def main():
    print(str(can_partition([1, 2, 3, 4])))
    print(str(can_partition([1, 1, 3, 4, 7])))  # [1,3,4] and [1,7]
    print(str(can_partition([2, 3, 4, 6])))


main()
