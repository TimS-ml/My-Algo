'''
Given a set of positive numbers, find the total number of subsets whose S is equal to a given number ‘S’.

# Code Explain:
- Time complexity: O(2^N)
- Space complexity: O(N)

lc 560

for each number 'i' 
  create a new set which includes number 'i' if it does not exceed 'S', and recursively   
      process the remaining numbers and S
  create a new set without number 'i', and recursively process the remaining numbers 
return the count of subsets who has a S equal to 'S'
'''


def count_subsets(nums, S):
    return count_subsets_recursive(nums, S, 0)


'''
for n in nums:
    number of solutions if choose n
    number of solutions if don't choose n
'''
def count_subsets_recursive(nums, S, idx):
    # base checks
    if S == 0:
        return 1
    n = len(nums)
    if n == 0 or idx >= n:
        return 0

    # recursive call after selecting the number at the idx
    # if the number at idx exceeds the S, we shouldn't process this
    sum1 = 0
    if nums[idx] <= S:
        sum1 = count_subsets_recursive(nums, S - nums[idx],
                                       idx + 1)

    # recursive call after excluding the number at the idx
    sum2 = count_subsets_recursive(nums, S, idx + 1)

    return sum1 + sum2


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
