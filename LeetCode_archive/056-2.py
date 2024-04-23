'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

Typical Sweep Line question, use heap for help
Mark every start as -1, every end as 1
Sort all start & end points
Close interval only when counter cur equals to 0
'''

import heapq
from typing import List


class Solution:
    '''
    this is similar as lc 253
    if s=1, e=-1, wrong
    1 1
    4 -1
    4 1
    5 -1

    if s=-1, e=1
    1 -1
    4 -1
    4 1
    5 1
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap, ans, = [], [] 
        for s, e in intervals:  # add start & end to heap (-1 is start, 1 is end)
            heapq.heappush(heap, (s, -1))
            heapq.heappush(heap, (e, 1))
        cur, s = 0, None            
        while heap:                            
            i, val = heapq.heappop(heap)       # pop heap
            if s is None: s = i                # is s is None, assign i to s (interval start)
            cur += val                         # keep counting until close interval
            if not cur:                        # when cur == 0, meaning we can close the interval
                ans.append([s, i])             # append interval to ans
                s = None                       # reset s to None
        return ans

