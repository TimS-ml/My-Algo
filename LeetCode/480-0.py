'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
import heapq
from collections import defaultdict


class Solution:
    # https://leetcode.com/problems/sliding-window-median/discuss/262689/Python-Small-and-Large-Heaps
    def medianSlidingWindow(self, nums, k):

        def move(h1, h2):
            x, i = heapq.heappop(h1)
            heapq.heappush(h2, (-x, i))

        def get_med(h1, h2, k):
            return h2[0][0] * 1. if k & 1 else (h2[0][0] - h1[0][0]) / 2.

        # first k elements: push in to maxHeap then pop k/2
        maxHeap, minHeap = [], []
        for i, x in enumerate(nums[:k]):
            heapq.heappush(maxHeap, (-x, i))
        for _ in range(k - (k >> 1)):
            move(maxHeap, minHeap)

        ans = [get_med(maxHeap, minHeap, k)]
        for i, x in enumerate(nums[k:]):
            if x >= minHeap[0][0]:
                heapq.heappush(minHeap, (x, i + k))
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
            ans.append(get_med(maxHeap, minHeap, k))
        return ans

    # https://leetcode.com/problems/sliding-window-median/discuss/394302/Python-clean-solution-(easy-to-understand)
    def medianSlidingWindow_2(self, nums: List[int], k: int) -> List[float]:
        if not nums or not k:
            return []
        maxHeap = []  # max heap
        minHeap = []  # min heap
        for i in range(k):
            if len(maxHeap) == len(minHeap):
                heapq.heappush(minHeap, -heapq.heappushpop(maxHeap, -nums[i]))
            else:
                heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, nums[i]))
        ans = [float(minHeap[0])] if k & 1 else [(minHeap[0] - maxHeap[0]) / 2.0]
        dicRemove = defaultdict(int)
        for i in range(k, len(nums)):  # right bound of window
            heapq.heappush(
                maxHeap, -heapq.heappushpop(minHeap, nums[i]))  # always push to maxHeap
            out_num = nums[i - k]
            if out_num > -maxHeap[0]:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            dicRemove[out_num] += 1
            while maxHeap and dicRemove[-maxHeap[0]]:
                dicRemove[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
            while dicRemove[minHeap[0]]:
                dicRemove[minHeap[0]] -= 1
                heapq.heappop(minHeap)
            if k % 2:
                ans.append(float(minHeap[0]))
            else:
                ans.append((minHeap[0] - maxHeap[0]) / 2.0)
        return ans
