# time: O(n)
# space: O(1)
# sorted, 2 pointers next_non_duplicate and i
# fast and slow pointers, swap value

def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 1
    while (i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]  # swap
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()


def remove_element(arr, key):
    nextElement = 0  # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]  # swap
            nextElement += 1

    return nextElement


def main_2():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " + str(remove_element([2, 11, 2, 2, 1], 2)))


main_2()
