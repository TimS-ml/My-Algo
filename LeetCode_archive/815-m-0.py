'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

undirection graph, weights = 1
adj dict
'''

from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        def buildGraph(routes):
            stopInfo = defaultdict(set)  # use set, there is dupl stops in single route
            for busId, route in enumerate(routes):
                for stop in route:
                    stopInfo[stop].add(busId)
            return stopInfo
        
        stopInfo = buildGraph(routes)

        q = deque()
        q.append(S)
        visited = set()

        ans = 0  # should start with 0!!!
        while q:
            for _ in range(len(q)):
                stop = q.popleft()
                
                if stop in visited:
                    continue
                else:
                    visited.add(stop)

                if stop == T:
                    return ans
                
                for busId in stopInfo[stop]:
                    for NxtStop in routes[busId]:
                        q.append(NxtStop)

            ans += 1

        return -1


# r = [[1,2,7],[3,6,7]]
# s, t = 1, 6

r = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
s, t = 15, 12

print(Solution().numBusesToDestination(r, s, t))
