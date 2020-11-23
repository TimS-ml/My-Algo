def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    isAscending = arr[start] < arr[end]
    while start <= end:
        # calculate the middle of the current range
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid

        if isAscending:  # ascending order
            if key < arr[mid]:
                end = mid - 1  # the 'key' can be in the first half
            else:  # key > arr[mid]
                start = mid + 1  # the 'key' can be in the second half
        else:  # descending order
            if key > arr[mid]:
                end = mid - 1  # the 'key' can be in the first half
            else:  # key < arr[mid]
                start = mid + 1  # the 'key' can be in the second half

    return -1  # element not found


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
