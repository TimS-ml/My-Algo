'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List
import collections


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int],
                               allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        G = [set() for i in range(n)]

        for i, j in allowedSwaps:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * n
        ans = 0

        def dfs(i):
            seen[i] = 1
            found.append(i)
            for j in G[i]:
                if seen[j]: continue
                dfs(j)

        for i in range(n):
            if seen[i]: continue
            found = []
            dfs(i)
            count1 = collections.Counter()
            count2 = collections.Counter()
            for j in found:
                count1[source[j]] += 1
                count2[target[j]] += 1
            ans += sum((count1 & count2).values())
        return n - ans
