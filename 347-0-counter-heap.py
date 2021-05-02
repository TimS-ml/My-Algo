'''

'''

from typing import List
from collections import Counter
from itertools import chain
from heapq import heapify, heappop, heappush


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        heap = []
        heapify(heap)
        for key in freq_dict:
            heappush(heap, [freq_dict[key], key])
            if len(heap) > k:
                heappop(heap)
        return [j for i, j in heap]

    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        counter_obj = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for key, freq in counter_obj.items():
            buckets[freq].append(key)
        result = list(chain(*buckets))
        return result[::-1][:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
