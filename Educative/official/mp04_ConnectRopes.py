'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

lc 1167

Always pick two of the smallest sticks to connect
'''

from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    minHeap = []
    # add all ropes to the min heap
    for i in ropeLengths:
        heappush(minHeap, i)

    # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
    # connect them and push the result back to the min heap.
    # keep doing this until the heap is left with only one rope
    result, temp = 0, 0
    while len(minHeap) > 1:
        temp = heappop(minHeap) + heappop(minHeap)
        result += temp
        heappush(minHeap, temp)

    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
