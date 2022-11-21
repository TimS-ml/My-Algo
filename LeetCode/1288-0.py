'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

the sorted() function in Python is implemented with the Timsort algorithm whose space complexity is O(N)
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        
        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prev_end:
                count += 1    
                prev_end = end
        
        return count
