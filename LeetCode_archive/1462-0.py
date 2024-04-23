'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)

        for a,b in prerequisites:
            adj_list[a].append(b)

        from functools import lru_cache
        @lru_cache(maxsize=None)
        def is_reachable(s,t):
            """s = source, t=target. Is target reachable from source?"""

            if s==t:
                return True

            for neighb in adj_list[s]:
                if is_reachable(neighb, t):
                    return True
            return False

        ans = []

        for s,t in queries:
            ans.append(is_reachable(s,t))

        return ans

    def checkIfPrerequisite_2(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0] * n
        pres = [set() for _ in range(n)]
        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
            pres[course].add(pre)
        queue = deque(course for course, degree in enumerate(in_degree)
                                  if degree == 0)
        while queue:
            pre = queue.popleft()
            for course in graph[pre]:
                pres[course] |= pres[pre]
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        return [pre in pres[course] for pre, course in queries]
