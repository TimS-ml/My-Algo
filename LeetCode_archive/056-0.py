'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(N)

'''

import heapq
from typing import List


class Solution:
    '''
    during looping: 
    - (fixed) prev_start <= start
    - if prev_end >= start, intersection
          (prevS, prevE)
                  (S,       E)

    - unlike lc 1288, end doesn't matter
          (prevS, prevE)
          (S,    E)

          (prevS, prevE)
          (S,              E)
    '''
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

    # using heap
    def merge_2(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)

        ans = []
        while intervals:
            cur = heapq.heappop(intervals)
            if ans and cur[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], cur[1])  # merge
            else:
                ans.append(cur)

        return ans


intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]
print(Solution().merge(intervals))
