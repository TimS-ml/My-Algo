'''
# Code Explain:
- Time complexity: O(N + klogN)
    - top k elements
- Space complexity: O(N)



'''

from typing import List
from collections import Counter
from itertools import chain
from heapq import heapify, heappop, heappush


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)

        # basically is sort by dic value, check 347-1
        heap = []
        heapify(heap)
        for key in freq_dict.keys():
            heappush(heap, [freq_dict[key], key])  # freq, char
            if len(heap) > k:
                heappop(heap)
        return [char for freq, char in heap]

    # no heap solution
    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for key, freq in freq_dict.items():
            buckets[freq].append(key)
        result = list(chain(*buckets))  # interesting...
        return result[::-1][:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
