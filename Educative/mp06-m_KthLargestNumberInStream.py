'''
# Code Explain:
- Time complexity: O(logK)
- Space complexity: O(K)

lc 703
'''

from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val):
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
