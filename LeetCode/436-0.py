'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List
import heapq


class Solution(object):
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # v = index, (start, end)
        left_sorted = sorted(enumerate(intervals),
                             key=lambda v: (v[1][0], v[0]))
        ans = [-1] * len(intervals)
        heap = []
        for idx, (start, end) in left_sorted:
            heapq.heappush(heap, (end, idx))
            # heap[0][0] = right bound of smallest value on the heap
            while heap and heap[0][0] <= start:  
                _, left_idx = heapq.heappop(heap)
                ans[left_idx] = idx
        return ans

    # Sorting + binary search. O(n log n) time O(n) space
    def findRightInterval_2(self, intervals):

        def bSearch(endpt, dic_sorted, i, j):
            while i < j:
                mid = (i + j) / 2
                if dic_sorted[mid][1].start == endpt:
                    return mid
                elif dic_sorted[mid][1].start > endpt:
                    j = mid
                else:
                    i = mid + 1
            return i

        if not intervals:
            return []
        elif len(intervals) == 1:
            return [-1]
        ans = [0] * len(intervals)
        dic = {i: intervals[i] for i in range(len(intervals))}
        dic_sorted = sorted(dic.items(), key=lambda x: x[1].start)
        for j, e in enumerate(dic_sorted):
            i, interval = e
            k = bSearch(interval.end, dic_sorted, j + 1, len(dic_sorted))
            if k == len(dic_sorted):
                ans[i] = -1
            else:
                ans[i] = dic_sorted[k][0]
        return ans

    # Sorting * 2 + linear scan. O(n log n) time O(n) space
    def findRightInterval_3(self, intervals):
        if not intervals:
            return []
        elif len(intervals) == 1:
            return [-1]
        ans = [-1] * len(intervals)
        dic = {i: intervals[i] for i in range(len(intervals))}
        dic_s = sorted(dic.items(), key=lambda x: x[1].start)
        dic_e = sorted(dic.items(), key=lambda x: x[1].end)
        j = 0
        for e in dic_e:
            i, interval = e
            while j < len(intervals) and dic_s[j][1].start < interval.end:
                j += 1
            if j == len(intervals):
                return ans
            ans[i] = dic_s[j][0]
        return ans
