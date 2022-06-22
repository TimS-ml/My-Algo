'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

- sorted array, don't know order
- asc or desc
- number exsit or not exsit
- number have dupl

Using:
- end = mid - 1
- start = mid + 1

Instead of (this will fall in to inf-loop):
- end = mid 
- start = mid
'''

def binary_search(arr, key):
    isAsc = arr[0] < arr[-1]
    start, end = 0, len(arr)-1

    while start <= end:
        # mid = int(start + (end - start) // 2)  # this is better
        mid = int((start + end) // 2)
        
        # or you can put mid here
        # if arr[mid] == key:
        #     return mid
        
        # we cannot do arr = arr[::-1]
        # since the time complexity is O(n)
        if isAsc:
            if key < arr[mid]:
                end = mid - 1
            elif key > arr[mid]:
                start = mid + 1
            else:  # arr[mid] == key
                return mid
        else:
            if key > arr[mid]:
                end = mid - 1
            elif key < arr[mid]:
                start = mid + 1
            else:  # arr[mid] == key
                return mid

    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()

