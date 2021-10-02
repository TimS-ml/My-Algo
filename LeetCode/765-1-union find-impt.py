'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
按对遍历, 若该对不是情侣, 将其分别对应的情侣对的编号进行联通同时计数加一

https://leetcode-cn.com/problems/couples-holding-hands/solution/bing-cha-ji-union-find-by-shty/
ans = 情侣对 - 环个数
- 最差的情况就是所有N对情侣都在一个环中, 这时候我们需要N - 1调换
- 最好情况每对情侣已经坐好了, 已经有N个大小为1的环, 这时候我们需要N - N次调换
'''

from typing import List


class Solution(object):
    def minSwapsCouples(self, row: List[int]) -> int:
        class Union:
            def __init__(self):
                self.parent = list(range(len(row) // 2))
                self.n = 0

            def union(self, x, y):
                t1, t2 = self.find(x), self.find(y)
                if t1 != t2:
                    self.parent[t1] = t2
                    self.n += 1  # 不联通, 计数+1

            def find(self, x):
                if self.parent[x] == x:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        u = Union()
        for i in range(0, len(row), 2):
            u.union(row[i] // 2, row[i + 1] // 2)
        return u.n
