'''
# Code Explain:
- Time complexity: O(N logM)
    - N=total number, M=num of input arrs
- Space complexity: O(M)

lc 632
'''

from heapq import *
import math


def find_smallest_range(lists):
    minHeap = []
    rangeStart, rangeEnd = 0, math.inf
    currentMaxNumber = -math.inf

    # put the 1st element of each array in the max heap
    for arr in lists:
        heappush(minHeap, (arr[0], 0, arr))
        currentMaxNumber = max(currentMaxNumber, arr[0])

    # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
    # if the array of the top element has more elements, insert the next element in the heap
    while len(minHeap) == len(lists):
        num, i, arr = heappop(minHeap)
        if rangeEnd - rangeStart > currentMaxNumber - num:
            rangeStart = num
            rangeEnd = currentMaxNumber

        # if next number is available
        if len(arr) > i + 1:
            # insert the next element in the heap
            heappush(minHeap, (arr[i + 1], i + 1, arr))
            currentMaxNumber = max(currentMaxNumber, arr[i + 1])

    return [rangeStart, rangeEnd]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
