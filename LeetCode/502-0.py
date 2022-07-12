'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
from heapq import nlargest, heappop, heappush

class Solution:
    # k: num of choose, w: init capital
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        # to speed up: if all projects are available
        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))
        
        n = len(Profits)
        projects = [(Capital[i], Profits[i]) for i in range(n)]
        # sort the projects :
        # the most available (= the smallest capital) is the last one
        projects.sort(key = lambda x : -x[0])
        
        available = []
        while k > 0:
            # update available projects
            while projects and projects[-1][0] <= W:
                heappush(available, -projects.pop()[1])
            # if there are available projects,
            # pick the most profitable one
            if available:
                W -= heappop(available)
            # not enough capital to start any project
            else:
                break
            k -= 1
        return W  
