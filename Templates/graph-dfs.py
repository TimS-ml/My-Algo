from typing import List
import collections

class Solution:
    # 323, undirected, count number of graphs
    def count_number_connection(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        # double directions
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, seen):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, seen)

        count = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                dfs(node, seen)
                count += 1
        return count

    # lc 737, check if connected
    def check_connected(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        graph = collections.defaultdict(set)
        for w1, w2 in pairs:
            graph[w1].add(w2)
            graph[w2].add(w1)
        
        def dfs(words1, words2, visited):
            for n in graph[words2]:
                if n in visited:
                    continue
                if words1 == n:
                    return True
                else:
                    visited.add(n)
                    if dfs(words1, n, visited):
                        return True
            return False

        for w1, w2 in zip(words1, words2):
            # w1 != w2 is important!!!
            if w1 != w2 and not dfs(w1, w2, set([w2])):
                return False
        return True


