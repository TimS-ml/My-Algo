'''
remove all duplicates from it
don't use any extra space
return length

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)


sorted, 2 pointers non_dupl_idx and i
fast and slow pointers, swap value

if swap rule is based on element, take care of edges (index 0 and -1)
'''

def remove_duplicates(arr):
    # index of the non-duplicate element
    # length = index + 1
    non_dupl_idx = 0
    i = 1
    while (i < len(arr)):
        # non_dupl_idx <= i
        # make sure the continuing value is different 
        if arr[non_dupl_idx] != arr[i]:
            arr[non_dupl_idx + 1] = arr[i]  # swap
            non_dupl_idx += 1
        i += 1
    # print(arr)
    return non_dupl_idx + 1

# or if you prefer this way
def remove_duplicates_2(arr):
    non_dupl_idx = 0
    for i in range(len(arr)):
        if arr[non_dupl_idx] != arr[i]:
            arr[non_dupl_idx + 1] = arr[i]  # swap
            non_dupl_idx += 1
    return non_dupl_idx + 1

def main():
    print(remove_duplicates_2([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates_2([2, 2, 2, 11]))


main()

'''
remove all instances of ‘key’ in-place and return the new length of the array

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)



'''

def remove_element(arr, key):
    next_elem = 0  # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_elem] = arr[i]  # swap, worth noticing that this is not idx+1
            next_elem += 1

    return next_elem


def main_2():
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_element([2, 11, 2, 2, 1], 2))


main_2()
