'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

double check if odd k, mid number (single one) is in minHeap or -maxHeap
'''

from heapq import *
import heapq


class SlidingWindowMedian:
    def find_sliding_window_median(self, nums, k):
        def move(h1, h2):
            x, i = heapq.heappop(h1)
            heapq.heappush(h2, (-x, i))

        def getMid(maxHeap, minHeap, k):
            # if len(maxHeap) != len(minHeap):
            if k % 2 == 1:
                return minHeap[0][0] * 1.0
            else:
                return (minHeap[0][0] - maxHeap[0][0]) / 2.0

        # first k elements: push in to maxHeap then pop k/2
        maxHeap, minHeap = [], []
        # init method 1
        # for i, x in enumerate(nums[:k]):
        #     heapq.heappush(maxHeap, (-x, i))
        # # note: int(3/2) = 1 !!!
        # for _ in range(k - int(k / 2)):
        #     move(maxHeap, minHeap)

        # init method 2
        for i in range(k):
            if len(maxHeap) == len(minHeap):
                heapq.heappush(maxHeap, (-nums[i], i))
                move(maxHeap, minHeap)
                # x, i = heapq.heappop(maxHeap)
                # heapq.heappush(minHeap, (-x, i))
            else:
                heapq.heappush(minHeap, (nums[i], i))
                move(minHeap, maxHeap)
                # x, i = heapq.heappop(minHeap)
                # heapq.heappush(maxHeap, (-x, i))

        ans = [getMid(maxHeap, minHeap, k)]
        for i, x in enumerate(nums[k:]):
            if x >= minHeap[0][0]:
                heapq.heappush(minHeap, (x, i + k))
                # nums[i]: left bound
                if nums[i] <= minHeap[0][0]:
                    move(minHeap, maxHeap)
            else:
                heapq.heappush(maxHeap, (-x, i + k))
                if nums[i] >= minHeap[0][0]:
                    move(maxHeap, minHeap)

            while maxHeap and maxHeap[0][1] <= i:
                heapq.heappop(maxHeap)
            while minHeap and minHeap[0][1] <= i:
                heapq.heappop(minHeap)
            ans.append(getMid(maxHeap, minHeap, k))
        return ans


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5],
                                                            2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5],
                                                            3)
    print("Sliding window medians are: " + str(result))


main()
