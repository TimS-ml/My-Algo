'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

lc 57 (insert + merge)
lc 987 (insert + intersection)

case:
 (a, b) (c, d) (e, f)
    (x,          y)

return (a, f)

three parts: before, merged, after
'''

from typing import List


class Solution:
    def insert(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]':
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        ans = []
        
        # before intersection
        while idx < n and new_start > intervals[idx][0]:
            ans.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # newInterval.start <= intervals[i].end
        # newInterval.start <= intervals[i].start (unlike sol2 and 3, this is known)

        # [... (a, b)] (c, d) (e, f)
        #         (x,          y)
        # this if else is dealing (a, b)

        # if there is no overlap, just add the interval
        # [... (a, b)]    (c, d) (e, f)
        #              (x,        y)
        # or
        # [... (a, b)] (c, d) (e, f)
        #      (x,             y)
        # or
        #      (a, b) (c, d) (e, f)
        #      (x,            y)
        if not ans or ans[-1][1] < new_start:
            ans.append(newInterval)
        # [... (a, b)] (c, d) (e, f)
        #         (x,          y)
        # or
        # [... (a,      b)] (c, d) (e, f)
        #         (x, y)
        else:
            ans[-1][1] = max(ans[-1][1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if ans[-1][1] < start:
                ans.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans

    def insert_2(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]':
        ans = []

        for i in range(len(intervals)):
            # end of the intersection
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                # before intersec + merged + end of intersec (intervals[i:])
                return ans + intervals[i:]
            # before intersection
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            # during intersection
            # newInterval.start <= intervals[i].end
            # newInterval.start ? intervals[i].start
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        ans.append(newInterval)
        return ans

    def insert_3(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]':
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [Interval(s, e)] + right
