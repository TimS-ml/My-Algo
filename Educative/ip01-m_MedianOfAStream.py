# Let's try len(minHeap) >= len(maxHeap)
# median = (min[0] + -max[0]) / 2

import heapq


class MedianOfAStream:
    def __init__(self):
        self.maxHeap = []  # first half
        self.minHeap = []  # second half

    def insert_num(self, num):
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            # max heap using -num
            heapq.heappush(self.maxHeap, -num)

        # balance
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def find_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return self.minHeap[0]


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
