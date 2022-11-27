'''
# Code Explain:
- Time complexity: O(E + V)
- Space complexity: O(E + V)

E = num of edges
V = num of vertices

'''

from typing import List

class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))


class Solution_2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry 
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})

    # UnionFind with Union by Rank
    def countComponents_2(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})
