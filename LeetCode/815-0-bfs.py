'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import defaultdict, deque
from sys import prefix


class Solution:
    def numBusesToDestination(self, routes, S, T):
        # routes[i][j] might not be unique? 
        to_routes = defaultdict(set)
        for busId, route in enumerate(routes):
            for stop in route:
                to_routes[stop].add(busId)

        # a not so common way of writing bfs...
        queue = [(S, 0)]
        seen = set([S])
        for stop, bus in queue:
            if stop == T: return bus
            for busId in to_routes[stop]:
                for transStop in routes[busId]:
                    if transStop not in seen:
                        queue.append((transStop, bus + 1))
                        seen.add(transStop)
                routes[busId] = []  # seen route

        return -1


    def numBusesToDestination_2(self, routes, S, T):
        # must have !!!
        if S == T:
            return 0

        # routes[i][j] might not be unique? 
        to_routes = defaultdict(set)
        for busId, route in enumerate(routes):
            for stop in route:
                to_routes[stop].add(busId)

        queue = deque([S])  # stop
        seen = set()  # busId

        ans = 0
        while queue:
            ans += 1

            # traverse all the current options
            # print(queue)
            preTrans = len(queue)
            for _ in range(preTrans):
                stop = queue.popleft()
                # print('stop:', stop)
                for busId in to_routes[stop]:
                    # print('bus:', busId)
                    if busId not in seen:
                        seen.add(busId)
                    else:
                        continue

                    for transStop in routes[busId]:
                        # print('transStop:', transStop)
                        if transStop == T:
                            return ans
                        queue.append(transStop)

        return -1


r = [[1,2,7],[3,6,7]]
s, t = 1, 6

print(Solution().numBusesToDestination_2(r, s, t))
