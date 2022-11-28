'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List

class Solution:
    def insert(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]':
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        # case: intervals = [[1,3],[6,9]], newInterval = [2,5]
        # output = [[1,3]], then will check end '3' and newInterval start '2'
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
