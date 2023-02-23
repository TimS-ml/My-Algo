'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    # Dijkstra
    def findCheapestPrice(self, n, flights, src, dst, k):
        # adj[srouce] = [[dest, feature]]]
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))

        visited = {}
        pq = [(0, 0, src)]  # cost, stops, node
        while pq:
            cost, stops, node = heapq.heappop(pq)
            if node == dst and stops - 1 <= k:
                return cost

            if node not in visited or visited[node] > stops:
                visited[node] = stops  # shortest
                for neighbor, price in adj[node]:
                    heapq.heappush(pq, (cost + price, stops + 1, neighbor))
        return -1

    # Dijkstra
    def findCheapestPrice_2(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))

        queue = deque()
        queue.append((src, 0))
        costs = [float("inf")] * n
        while queue and k >= 0:
            m = len(queue)
            for _ in range(m):
                curr, cost = queue.popleft()
                for node, price in adj[curr]:
                    if cost + price < costs[node]:
                        costs[node] = cost + price
                        queue.append((node, costs[node]))
            k -= 1

        return costs[dst] if costs[dst] != float("inf") else -1

