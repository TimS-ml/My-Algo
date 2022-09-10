'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 33

difference between kp08 and kp09:

kp09 is a sorted array then split half then combine
case: ASC arr: [a, b, c, d], rotate: [c, d, a, b]
any number in c~d > any number in a~b

kp08: [e, f, g]
can't compare any number in e~f vs any number in f~g
'''

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:  # left side is sorted in ascending order
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
