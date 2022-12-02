'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(N)

intervals intersection
we don't care the connection in [start, end], we only care about max number of overlap
'''

import heapq
from typing import List


class Solution:
    # Chronological Ordering
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begin = [meet[0] for meet in intervals]
        end = [meet[1] for meet in intervals]

        begin.sort()
        end.sort()

        count = 0
        ans, i, j = 0, 0, 0

        while (i < len(intervals) and j < len(intervals)):
            if begin[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)

        return ans


    # Chronological Ordering
    '''
    this is similar as lc 56-2
    input: [[0, 30], [5, 10], [15, 20]]
    out  : [[0, 1], [5, 1], [10, -1], [15, 1], [20, -1], [30, -1]]
    '''
    def minMeetingRooms_2(self, intervals: List[List[int]]) -> int:
        room = []
        for meet in intervals:
            room.append([meet[0], 1])
            room.append([meet[1], -1])
        
        room = sorted(room, key=lambda x: (x[0], x[1]))
        count = 0
        ans = 0
        
        for i in range(len(room)):
            count += room[i][1]
            ans = max(ans, count)

        return ans


    # Priority Queues
    # equal to sort the end
    def minMeetingRooms_3(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap = []  # min heap, stores the end time of intervals
        for meet in intervals:
            if heap and meet[0] >= heap[0]:
                # means two intervals can use the same room
                # curr.start >= prev.end
                heapq.heapreplace(heap, meet[1])  # pop + push
            else:
                # a new room is allocated
                heapq.heappush(heap, meet[1])
        return len(heap)
