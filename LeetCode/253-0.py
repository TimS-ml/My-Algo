'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(N)

intervals intersection pattern
'''

import heapq

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


    # Priority Queues
    def minMeetingRooms_2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for meet in intervals:
            if heap and meet.start >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, meet.end)  # pop + push
            else:
                # a new room is allocated
                heapq.heappush(heap, meet.end)
        return len(heap)
