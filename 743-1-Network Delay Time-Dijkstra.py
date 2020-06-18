# https://leetcode-cn.com/problems/network-delay-time/

import heapq
import collections


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # O(ElgV) E edges, V vertices
        # Dijkstra's
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
        print(graph)
        pq = [[0, K]]
        dic = dict()

        # len(pq) ~ V
        while pq:
            distance, node = heapq.heappop(pq)
            # visited
            if node in dic:
                continue
            dic[node] = distance
            print(dic)
            # O(E) ~ edges
            for desination, path in graph[node]:
                if desination not in dic:
                    heapq.heappush(pq, (distance + path, desination))
                    print(dic, pq)
        return max(dic.values()) if len(dic) == N else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2  # start point
print(Solution().networkDelayTime(times, N, K))
