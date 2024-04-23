'''
# Code Explain:
get mid
- Time complexity: O(1)
- Space complexity: O(1)

add
- Time complexity: O(logN)
- Space complexity: O(N)

two cases
[1] small = [1, 2, 3], large = [4]  -> rebalance
[1] small = [1, 7], large = [4, 6]  -> move 7 to large, then rebalance
'''

from heapq import heappush, heappop, heappushpop


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
