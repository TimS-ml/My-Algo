'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''

from typing import List
from collections import Counter, defaultdict


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int],
                               allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = {i: i for i in range(n)}

        # disjoint set
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # 搜索根节点
        for l, r in allowedSwaps:
            a, b = find(l), find(r)
            if a != b:
                parent[b] = a

        # 获取根节点对应的连通块
        dic = defaultdict(list)
        for i in range(n):
            a = find(i)
            dic[a].append(i)
        ans = 0

        # 计算每个连通块对应的source元素与target的差集
        for k, v in dic.items():
            a = [source[i] for i in v]
            b = Counter([target[i] for i in v])
            for c in a:
                if b[c] > 0:
                    b[c] -= 1
                else:
                    ans += 1
        return ans
