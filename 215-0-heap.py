'''
# Thought process
[1] sort the list
[2] located the kth number
  - 1st largest number is at sorted[0]

# Test cases
3,2,3,1,2,4,5,5,6
4

'''

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        # print(nums)
        return nums[k - 1]

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for num in nums:
            # build heap
            heappush(heap, num)

            # !!! this will only keep k largest numbers from array
            if len(heap) > k:
                heappop(heap)

        # pick minimum among k largest numbers
        return heappop(heap)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(Solution().findKthLargest_2(nums, k))
