'''
# Code Explain:
- Time complexity: O(NP)  N=max(len1, len2), P=size of Pairs
- Space complexity: O(P)

case:
["1","2","3","4","5","6"]
["1","2","3","4","5","6"]
[]
'''

from typing import List
import collections


class Solution:
    # dfs
    def are_sentences_similar_two(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
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


    # bfs
    def are_sentences_similar_two_2(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        graph = collections.defaultdict(list)
        for w1, w2 in pairs:
            graph[w1].append(w2)
            graph[w2].append(w1)

        for w1, w2 in zip(words1, words2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2: break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True
