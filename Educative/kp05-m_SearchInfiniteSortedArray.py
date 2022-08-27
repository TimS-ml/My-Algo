'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

basic binary search
'''

import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, target):
    # find the proper bounds first
    left, right = 0, 1
    while reader.get(right) < target:
        left = right  # shrink start is better, but won't affect complexity
        # right = right ** 2
        right <<= 1  # right start with 1, so = r ** 2 won't work
    
    # print(left, right)
    while left < right:
        mid = left + (right - left) // 2
        if reader.get(mid) == target:
            return mid
        elif reader.get(mid) < target:
            left = mid + 1
        elif reader.get(mid) > target:
            right = mid

    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))

    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
