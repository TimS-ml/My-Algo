'''
# Code Explain:
- Time complexity: O(N logK)
It's O(N log2K) slower than quick sort
- Space complexity: O(K)

easy way: nums.sort(reverse=True), time: O(N * log(N))

Sol: min heap => pop largest
in python, heappop will pop minimum value

case:
3,2,3,1,2,4,5,5,6
4

'''

from typing import List
import heapq
from heapq import heapify, heappush, heappop


class Solution:
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

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(Solution().findKthLargest(nums, k))
