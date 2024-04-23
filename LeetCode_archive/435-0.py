'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(1)

'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # sort by start is ok
        ans = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # non-overlapping
            if start >= prevEnd:
                prevEnd = end
            # [1] the best rule to achieve minimum del is not (non-overlapping)
            #     which is min End
            # [2] we don't need to modify the array, only return the count
            else:
                ans += 1
                prevEnd = min(end, prevEnd)
        return ans
