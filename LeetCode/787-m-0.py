'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

case:
- not connected
- src != dst
- price >= 0

sol 1
dp[i] = min price from src to city i within k
'''

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        for _ in range(k + 1):
            tmp = dp.copy()
            for s, d, p in flights:  # start, dest, price
                if dp[s] == float('inf'):
                    continue

                # connected
                # if dp[s] + p < tmp[d]:
                #     tmp[d] = dp[s] + p
                # !!! if not using tmp[d], then the point d may be updated multiple times
                # say dp[3] = 100, 1->3 = 80, 2->3 = 90
                # if min(dp[d], dp[s] + p), then the output might be 90
                tmp[d] = min(tmp[d], dp[s] + p)

            dp = tmp

        if dp[dst] == float('inf'):
            return -1
        return dp[dst]


    # bfs
    def findCheapestPrice_2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)  # not defaultdict(list)!!!
        for s, d, price in flights:
            graph[s][d] = price

        # we might go through same city multiple times, with different [cost, step]
        heap = [(0, src, k + 1)]
        while heap:
            price, city, step = heapq.heappop(heap)  # must use heap!!!
            print(price, city, step)
            if city == dst:
                return price
            if step > 0:
                for j in graph[city]:
                    heapq.heappush(heap, (price + graph[city][j], j, step - 1))
        return -1



n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# src, dst, k = 0, 3, 1
src, dst, k = 0, 3, 9

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src, dst, k = 0, 2, 1

print(Solution().findCheapestPrice_2(n, flights, src, dst, k))
