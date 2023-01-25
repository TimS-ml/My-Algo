'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class DSU:
    def __init__(self, N):
        self.p = range(N)
        self.sz = [1] * N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        self.sz[yr] += self.sz[xr]

    def size(self, x):
        return self.sz[self.find(x)]


class Solution(object):
    def minMalwareSpread(self, graph, initial):
        dsu = DSU(len(graph))

        for j, row in enumerate(graph):
            for i in xrange(j):
                if row[i]:
                    dsu.union(i, j)

        count = collections.Counter(dsu.find(u) for u in initial)
        ans = (-1, min(initial))
        for node in initial:
            root = dsu.find(node)
            if count[root] == 1:  # unique color
                if dsu.size(root) > ans[0]:
                    ans = dsu.size(root), node
                elif dsu.size(root) == ans[0] and node < ans[1]:
                    ans = dsu.size(root), node

        return ans[1]
