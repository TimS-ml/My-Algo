'''
# Code Explain:
- Time complexity: O(NlogK)
- Space complexity: O(K)

k largest -> update smallest -> min heap heap[0]
well you can use max heap then pop top 3, but then the time complexity is NlogN
'''

from heapq import *


def find_k_largest_numbers(nums, k):
    minHeap = []

    # init
    for i in range(k):
        heappush(minHeap, nums[i])

    # update
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
