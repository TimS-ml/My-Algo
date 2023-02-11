'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from heapq import heappush, heappop
from collections import defaultdict, deque


class Solution(object):
    # normal bfs, similar to SPFA
    def networkDelayTime(self, times, N, K):
        elapsedTime = [0] + [float("inf")] * N
        graph = defaultdict(list)
        queue = deque([(0, K)])  # time, node

        # source, target, time
        for u, v, w in times:
            graph[u].append((v, w))

        while queue:
            time, node = queue.popleft()
            # check time benefits at current node
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1

    # Shortest Path Faster Algorithm (SPFA), replace Dijkstra heap to queue
    def networkDelayTime_2(self, times, N, K):
        elapsedTime = [0] + [float("inf")] * N
        graph = defaultdict(list)
        queue = deque([(0, K)])  # time, node
        elapsedTime[K] = 0

        for u, v, w in times:
            graph[u].append((v, w))

        while queue:
            time, node = queue.popleft()
            for v, w in graph[node]:
                # check time benefits moving to next step
                if time + w < elapsedTime[v]:
                    elapsedTime[v] = time + w
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1

    # Dijkstra bfs
    def networkDelayTime_3(self, times, N, K):
        elapsedTime = [0] + [float("inf")] * N
        graph = defaultdict(list)
        heap = [(0, K)]  # it's a min-heap: time, node

        for u, v, w in times:
            graph[u].append((v, w))

        while heap:
            time, node = heappop(heap)
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    heappush(heap, (time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1

    # dfs (basically rewrite of dfs)
    def networkDelayTime_4(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distance = {node: float("inf") for node in range(1, N + 1)}
        self.DFS(graph, distance, K, 0)
        totalTime = max(distance.values())
        return totalTime if totalTime < float("inf") else -1

    def DFS(self, graph, distance, node, elapsedTimeSoFar):
        if elapsedTimeSoFar >= distance[
                node]:  # signal aalreaady reached to this node. so no need to explore for this node
            return
        distance[node] = elapsedTimeSoFar
        for v, w in sorted(graph[node]):
            self.DFS(graph, distance, v, elapsedTimeSoFar + w)


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2  # start point
print(Solution().networkDelayTime(times, N, K))
