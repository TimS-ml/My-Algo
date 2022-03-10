'''
# Code Explain:
sol 2: pickIndex
- Time complexity: O(log n)
- Space complexity: O(1)

'''

from typing import List
import itertools, random


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        presum = 0
        for weight in w:
            presum += weight
            self.prefix_sums.append(presum)
        self.total_sum = presum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, presum in enumerate(self.prefix_sums):
            if target < presum:
                return i

class Solution2:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        presum = 0
        for weight in w:
            presum += weight
            self.prefix_sums.append(presum)
        self.total_sum = presum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
