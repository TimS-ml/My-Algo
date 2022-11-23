'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

lc 702

find bounds then binary_search

we can calc worst search time:
secret = [-1,0,3,5,9,12], target = 9,
worst time = target - 1st val = 9 - (-1) = 10
'''

import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # find the proper bounds first
    start, end = 0, 1
    while reader.get(end) < key:
        newStart = end + 1
        end += (end - start + 1) * 2  # this is not so good implementation actually
        # increase to double the bounds size
        start = newStart

    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if key < reader.get(mid):
            end = mid - 1
        elif key > reader.get(mid):
            start = mid + 1
        else:  # found the key
            return mid

    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
