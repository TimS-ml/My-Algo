'''
# Code Explain:
- Time complexity: O(EK)  E is number of edges in the graph
- Space complexity: O()

'''

from typing import List

class Solution:
    # bellman ford
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            # !!! because the calc dp[d] was based on previous price
            # if we just do inplace copy it will mass up the dp update
            # say we need to compare: [a] s=1, d=2; [b] s=2, d=3
            # and if in place, then we update dp[2] after [a], it will affect [b] (make more than 1 move per loop)
            tmpPrices = prices.copy()

            # at step 1, the p[src]!=inf, only update the node with s=0
            # say src connected with node a and b
            # at step 2, not inf node is src, a, b
            for s, d, p in flights:  # s=source, d=dest, p=price
                # only check connected node
                # this node is unable to reach
                if prices[s] == float("inf"):
                    continue

                # found a lower cost path
                # !!! if not using tmp[d], then the point d may be updated multiple times
                # say dp[3] = 100, 1->3 = 80, 2->3 = 90
                # if min(dp[d], dp[s] + p), then the output might be 90
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]

