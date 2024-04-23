'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import heapq
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort()
        slots2.sort()
        pointer1 = pointer2 = 0

        while pointer1 < len(slots1) and pointer2 < len(slots2):
            # find the boundaries of the intersection, or the common slot
            intersect_right = min(slots1[pointer1][1], slots2[pointer2][1])
            intersect_left = max(slots1[pointer1][0],slots2[pointer2][0])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]
            # always move the one that ends earlier
            if slots1[pointer1][1]< slots2[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
        return []

    # heap
    def minAvailableDuration_2(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # build up a heap containing time slots last longer than duration
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []
