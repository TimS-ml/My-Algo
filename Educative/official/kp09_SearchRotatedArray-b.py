'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

with dupl
'''


def search_rotated_with_duplicates(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        # the only difference from the previous solution,
        # if numbers at indexes start, mid, and end are same, we can't choose a side
        # the best we can do, is to skip one number from both ends as key != arr[mid]
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1
        elif arr[start] <= arr[mid]:  # left side is sorted in ascending order
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:  # key > arr[mid]
                start = mid + 1

        else:  # right side is sorted in ascending order
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    # we are not able to find the element in the given array
    return -1


def main():
    print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


main()
