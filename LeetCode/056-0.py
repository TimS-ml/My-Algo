'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(N)

'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # sort by start
        # intervals.sort()  # this is OK actually
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            # if overlap, find the largest right edge
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans

intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]
print(Solution().merge(intervals))
