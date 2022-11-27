'''
# Code Explain:
- Time complexity: O(V + E)
- Space complexity: O(V + E)

'''

class Solution:
    def validTree(self, n, edges):
        group = [i for i in range(n)]
        for e1, e2 in edges:
            root1 = self.find(e1, group)
            root2 = self.find(e2, group)
            if root1 == root2:
                return False
            else:
                group[root2] = root1
        return len(edges) == n - 1
    
    def find(self, e, group):
        if e == group[e]:
            return e
        else:
            return self.find(group[e], group)

    def validTree_2(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
