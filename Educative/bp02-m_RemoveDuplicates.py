'''
remove all duplicates from it
don't use any extra space
return length

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

lc 026
fast and slow pointers pattern
reverse array pattern
'''

# swap exclude 1st element
def remove_duplicates(arr):
    fast, slow = 0, 0
    while fast < len(arr):
        if arr[fast] != arr[slow]:  # now fast is ahead slow
            arr[slow + 1] = arr[fast]
            slow += 1
        fast += 1

    return slow + 1


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    # print(remove_duplicates([2, 3, 3, 11]))
    # print(remove_duplicates([1, 2, 3, 4]))


main()

'''
unsorted array
remove all instances of 'key' in-place
return the new length of the array

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

lc 027
'''

# swap include 1st element
def remove_element(arr, key):
    fast, slow = 0, 0
    while fast < len(arr):
        if arr[fast] != key:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1

    return slow


def main_2():
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_element([2, 11, 2, 2, 1], 2))


main_2()
