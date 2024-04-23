'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


# union find
class Solution:
    def numIslands2(self, m: int, n: int,
                    positions: List[List[int]]) -> List[int]:

        def find(p):
            while p in parent:
                if parent[p] in parent:  # path compress
                    parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p1, p2):
            pax, pay = find(p1), find(p2)
            if pax == pay:  # union fail,has been unioned.
                return False
            parent[pax] = pay
            return True

        seen, parent = set(), {}
        ans, count = [], 0
        for x, y in positions:  # connect with neighbor val==1,if union success,means one island disappear.
            if (x, y) not in seen:
                seen.add((x, y))
                count += 1
                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (i, j) in seen and union((i, j), (x, y)):
                        count -= 1
            ans.append(count)
        return ans
