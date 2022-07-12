'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 295
'''

# The time complexity of the insertNum() will be O(logN)
#   due to the insertion in the heap
# The time complexity of the findMedian() will be O(1)
#   as we can find the median from the top elements of the heaps
# space: O(N)

# Min heap and max heap
# heapq is _min heap_, to use max heap, invert the value of the keys and use heapq
# since min heap [0] return the smallest element, it should be put in bigger half
# We let 1 >= len(maxHeap) - len(minHeap) >= 0

import heapq


class MedianOfAStream:
    def __init__(self):
        self.minHeap = []  # second half
        self.maxHeap = []  # first half

    def insert_num(self, num):
        # Insert number
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            print('Max heap', self.maxHeap, self.maxHeap[0])
        else:
            heapq.heappush(self.minHeap, num)
            print('Min heap', self.minHeap, self.minHeap[0])

        # Check length
        if len(self.maxHeap) < len(self.minHeap):
            # move top of minHeap to maxHeap
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            median = (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            median = -self.maxHeap[0]
        return median


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))  # 2
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))  # 3
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))  # 3.5


main()
