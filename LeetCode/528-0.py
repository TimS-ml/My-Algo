'''
# Code Explain:
sol 2: pickIndex
- Time complexity: O(logN)
- Space complexity: O(1)

- If float rand (i.e. between [0, 1) range), use totalSum * random()
- If in range (i.e. INT only), use randint(1, totalSum), do not include 0 !!!

In this question preSum does not need leading 0 actually...
'''

from typing import List
import itertools, random


class Solution:
    def __init__(self, w: List[int]):
        self.preSum = []
        s = 0
        for weight in w:
            s += weight
            self.preSum.append(s)
        self.totalSum = s

    def pickIndex(self) -> int:
        target = self.totalSum * random.random()
        # run a linear search to find the target zone
        for i, s in enumerate(self.preSum):
            if target < s:
                return i


class Solution2:
    def __init__(self, w: List[int]):
        self.preSum = [0]
        s = 0
        for weight in w:
            s += weight
            self.preSum.append(s)
        self.totalSum = s

    def pickIndex(self) -> int:
        target = self.totalSum * random.random()  # [0~1)
        # run a binary search to find the target zone
        # left bound
        low, high = 0, len(self.preSum)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.preSum[mid]:
                low = mid + 1
            else:  # target <= self.preSum[mid]
                high = mid
        return low - 1

    def pickIndex_b(self) -> int:
        target = self.totalSum * random.random()  # [0~1)
        # run a binary search to find the target zone
        # left bound
        low, high = 0, len(self.preSum) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target > self.preSum[mid]:
                low = mid + 1
            elif target <= self.preSum[mid]:
                high = mid - 1
        # if left >= len(self.preSum):
        #     return -1
        return low - 1


# Let's use randint
class Solution3:
    def __init__(self, w: List[int]):
        self.preSum = [0]
        s = 0
        for weight in w:
            s += weight
            self.preSum.append(s)

    def pickIndex(self) -> int:
        target = random.randint(1, self.preSum[-1])  # [1~self.totalSum]
        # run a binary search to find the target zone
        # left bound
        low, high = 0, len(self.preSum) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target > self.preSum[mid]:
                low = mid + 1
            elif target <= self.preSum[mid]:
                high = mid - 1
        # if left >= len(self.preSum):
        #     return -1
        return low - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
