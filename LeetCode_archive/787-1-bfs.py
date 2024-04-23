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
            # we MUST use heap, and put cost at first
            # min heap, pop smallest cost
            # this will make sure when we first arrive dst, it's the smallest cost
            # case:
            #   n = 4
            #   flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,100],[2,3,200]]
            #   src, dst, k = 0, 3, 9
            # at 2nd move, $100 1->2 will move first, but $100 1->3 will arrive first
            cost, stops, node = heapq.heappop(pq)
            print(cost, stops, node, pq)

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




# n = 4
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# # src, dst, k = 0, 3, 1
# src, dst, k = 0, 3, 9

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,100],[2,3,200]]
src, dst, k = 0, 3, 9

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src, dst, k = 0, 2, 1

print(Solution().findCheapestPrice(n, flights, src, dst, k))
