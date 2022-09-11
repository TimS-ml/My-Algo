'''
# Code Explain:
- Time complexity: O(NlogK)
- Space complexity: O(K)

Note: return kth not top k
'''

from heapq import *

def find_Kth_smallest_number(nums, k):
    maxHeap = []

    # init
    for i in range(k):
        heappush(maxHeap, -nums[i])

    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    return -maxHeap[0]
