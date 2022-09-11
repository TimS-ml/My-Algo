'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

The tricky part is to figure out the pattern of minimum cost
'''

from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    # minHeap = []
    # for i in ropeLengths:
    #     heappush(minHeap, i)

    minHeap = ropeLengths
    heapify(minHeap)

    result, temp = 0, 0
    while len(minHeap) > 1:  # make sure at lease 2 elements in the heap
        # pop top two
        temp = heappop(minHeap) + heappop(minHeap)
        result += temp
        heappush(minHeap, temp)

    # here: heap = [temp]
    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
