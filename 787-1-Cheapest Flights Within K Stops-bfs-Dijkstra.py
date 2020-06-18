# https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import collections
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # O(ElgV) E flight ways ,V cities
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p  # flight a->b prize=p

        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                # bfs
                # {1: 100, 2: 150} [(100, 1, 1)]
                # {1: 100, 2: 150} [(100, 1, 1), (150, 2, 1)]
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
                    print(f[i], heap)
        return -1


n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 150]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, edges, src, dst, k))
