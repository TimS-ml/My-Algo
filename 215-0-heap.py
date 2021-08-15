'''
# Thought process
[1] sort the list
  - easy way: nums.sort(reverse=True), time: O(N * log(N))
  - heapq in python: O(N * log(2N))
    - in python, heappop will pop minimum value
  - Merge Sort or Quick Sort: O(N * log(N))
[2] located the kth number
  - k start at 1

# Test cases
3,2,3,1,2,4,5,5,6
4

'''

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort(reverse=True)
    #     # print(nums)
    #     return nums[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for num in nums:
            # build heap
            heappush(heap, num)

            # !!! this will only keep k largest numbers from array
            if len(heap) > k:
                heappop(heap)
                # print(heappop(heap))

        # pick minimum among k largest numbers
        return heappop(heap)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(Solution().findKthLargest(nums, k))
