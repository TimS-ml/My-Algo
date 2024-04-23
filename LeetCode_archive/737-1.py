'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import itertools


class Solution:
    def are_sentences_similar_two(self, words1: List[str], words2: List[str],
                                  pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        index = {}
        count = itertools.count()
        dsu = DSU(2 * len(pairs))
        for pair in pairs:
            for p in pair:
                if p not in index:
                    index[p] = next(count)
            dsu.union(index[pair[0]], index[pair[1]])

        return all(w1 == w2 or w1 in index and w2 in index
                   and dsu.find(index[w1]) == dsu.find(index[w2])
                   for w1, w2 in zip(words1, words2))


class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)
