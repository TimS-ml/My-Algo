'''
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:
range from 0 to n

case: arr = [4, 0, 3, 1]
4 < len(arr) will be skiped during the sort, basically we put the largest value (4) into the missing value positon (3rd, where '2' located)
'''


def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    print(nums)
    # find the first number missing from its index, 
    # that will be our required number
    for i in range(n):
        if nums[i] != i:
            return i

    return n


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
