'''
# Code Explain:
- Time complexity: O(K^2 logK)
    - when both arrays have at least K elements
    - otherwise, O(N M logK)
- Space complexity: O(K)

lc 373
'''

from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    minHeap = []
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(minHeap) < k:
                heappush(minHeap, (nums1[i] + nums2[j], i, j))
            else:
                # If the sum of the two numbers from the two arrays is smaller than the smallest(top)
                # element of the heap, we can 'break' here.
                # Since the arrays are sorted in the
                # descending order, we'll not be able to find a pair with a higher sum moving forward
                if nums1[i] + nums2[j] < minHeap[0][0]:
                    break
                else:
                    # we have a pair with a larger sum, remove top and insert this pair in the heap
                    heappop(minHeap)
                    heappush(minHeap, (nums1[i] + nums2[j], i, j))

    result = []
    for (num, i, j) in minHeap:
        result.append([nums1[i], nums2[j]])

    return result


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
