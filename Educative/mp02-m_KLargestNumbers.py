'''
# Code Explain:
- Time complexity: O(NlogK)
- Space complexity: O(K)

well you can use max heap then pop top 3, but then the time complexity is NlogN

top3 largest -> update the smallest
'''

from heapq import *

def find_k_largest_numbers(nums, k):
    minHeap = []

    # init
    for i in range(k):
        heappush(minHeap, nums[i])

    # update top k
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappushpop(minHeap, nums[i])

    return list(minHeap)
