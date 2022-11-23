'''
Given a set of positive numbers, find the total number of subsets whose S is equal to a given number 'S'.

# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 560
'''


# top down
def count_subsets(nums, S):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(S + 1)] for y in range(len(nums))]
    return count_subsets_recursive(dp, nums, S, 0)


def count_subsets_recursive(dp, nums, S, idx):
    # base checks
    if S == 0:
        return 1

    n = len(nums)
    if n == 0 or idx >= n:
        return 0

    # check if we have not already processed a similar problem
    if dp[idx][S] == -1:
        # recursive call after choosing the number at the idx
        # if the number at idx exceeds the S, we shouldn't process this
        sum1 = 0
        if nums[idx] <= S:
            sum1 = count_subsets_recursive(dp, nums, S - nums[idx],
                                           idx + 1)

        # recursive call after excluding the number at the idx
        sum2 = count_subsets_recursive(dp, nums, S, idx + 1)

        dp[idx][S] = sum1 + sum2

    return dp[idx][S]


# bottom up
def count_subsets_2(nums, S):
    n = len(nums)
    dp = [[-1 for x in range(S + 1)] for y in range(n)]

    # populate the S = 0 columns, as we will always have an empty set for zero S
    for i in range(0, n):
        dp[i][0] = 1

    # with only one number, we can form a subset only when the required S is
    # equal to its value
    for s in range(1, S + 1):
        dp[0][s] = 1 if nums[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(1, S + 1):
            # exclude the number
            dp[i][s] = dp[i - 1][s]
            # include the number, if it does not exceed the S
            if s >= nums[i]:
                dp[i][s] += dp[i - 1][s - nums[i]]

    # the bottom-right corner will have our answer.
    return dp[n - 1][S]


def count_subsets_rolling(nums, S):
    n = len(nums)
    dp = [0 for x in range(S + 1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required S is equal to the number
    for s in range(1, S + 1):
        dp[s] = 1 if nums[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(S, -1, -1):
            if s >= nums[i]:
                dp[s] += dp[s - nums[i]]

    return dp[S]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
