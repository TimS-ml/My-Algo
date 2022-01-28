'''
# Code Explain:
- Time complexity: O(N * S)
- Space complexity: O(N * S)

# Pros and Cons and Notation:

Bottom-up Dynamic Programming
'''


def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [[False for x in range(int(s / 2) + 1)] for y in range(n)]

    # populate the s=0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to that number
    for j in range(0, int(s / 2) + 1):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s / 2) + 1):
            # if we can get the sum 's' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]

    sum1 = 0
    # find the largest index in the last row which is true
    for i in range(int(s / 2), -1, -1):
        if dp[n - 1][i]:
            sum1 = i
            break

    sum2 = s - sum1
    return abs(sum2 - sum1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
