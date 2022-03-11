'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

This is a great example on how ultimately the start, end, mid will go when key is not in arr
- Asc array
- find ceiling (smallest element in the given array greater than or equal to the ‘key’.)
'''

def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = int((start + end) // 2)
        
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid+1]
            return mid

    # since the loop is running until 'start <= end', 
    # so at the end of the while loop, 'start == end+1' (start > end)
    # we are not able to find the element in the given array, 
    # so the next big number will be arr[start]
    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()

