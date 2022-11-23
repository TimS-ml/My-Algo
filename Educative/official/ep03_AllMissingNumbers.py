'''
We are given an unsorted array containing numbers taken from the range 1 to 'n'.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)



same as ep02
the key concept is that ignore about the duplicates, all you need is to put the correct into correct position
i.e.:
[1] the missing numbers (ans) are replaced with duplicates
[2] exist connection between value and index
'''


def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    print(nums)
    missingNumbers = []

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))  # 4, 6, 7
    print(find_missing_numbers([2, 4, 1, 2]))  # 3
    print(find_missing_numbers([2, 3, 2, 1]))  # 4


main()
