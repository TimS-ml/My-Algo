'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Adjacency list

'seen (visited)' can use either stop or busId
'''

from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes, S, T):
        # routes[i][j] might not be unique? 
        stopInfo = defaultdict(set)
        for busId, route in enumerate(routes):
            for stop in route:
                stopInfo[stop].add(busId)

        # dijkstra way of writing bfs...
        # unable to track level length, so need additional val to track depth
        queue = [(S, 0)]
        seen = set([S])
        for stop, bus in queue:
            if stop == T: return bus
            for busId in stopInfo[stop]:
                for transStop in routes[busId]:
                    if transStop not in seen:
                        queue.append((transStop, bus + 1))
                        seen.add(transStop)
                routes[busId] = []  # seen route

        return -1

    def numBusesToDestination_1b(self, routes, S, T):
        # routes[i][j] might not be unique? 
        stopInfo = defaultdict(set)
        for busId, route in enumerate(routes):
            for stop in route:
                stopInfo[stop].add(busId)

        # a not so common way of writing bfs...
        # unable to track level length, so need additional val to track depth
        queue = [(S, 0)]
        seen = set()
        for stop, bus in queue:
            if stop == T: return bus
            for busId in stopInfo[stop]:
                if busId not in seen:
                    seen.add(busId)
                else:
                    continue
                for transStop in routes[busId]:
                    queue.append((transStop, bus + 1))
                routes[busId] = []  # seen route

        return -1


    def numBusesToDestination_2(self, routes, S, T):
        # must have !!!
        if S == T:
            return 0

        # routes[i][j] might not be unique? 
        stopInfo = defaultdict(set)
        for busId, route in enumerate(routes):
            for stop in route:
                stopInfo[stop].add(busId)

        queue = deque([S])  # stop
        seen = set()  # busId

        ans = 0
        while queue:
            ans += 1

            # traverse all the current options
            preTrans = len(queue)
            for _ in range(preTrans):
                stop = queue.popleft()
                for busId in stopInfo[stop]:
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


    def numBusesToDestination_2b(self, routes, S, T):
        # routes[i][j] might not be unique? 
        stopInfo = defaultdict(set)
        for busId, route in enumerate(routes):
            for stop in route:
                stopInfo[stop].add(busId)

        queue = deque([S])  # stop
        seen = set()  # busId

        ans = 0
        while queue:
            # traverse all the current options
            preTrans = len(queue)
            for _ in range(preTrans):
                stop = queue.popleft()
                if stop == T:
                    return ans
                for busId in stopInfo[stop]:
                    if busId not in seen:
                        seen.add(busId)
                    else:
                        continue

                    for transStop in routes[busId]:
                        queue.append(transStop)
            ans += 1

        return -1


r = [[1,2,7],[3,6,7]]
s, t = 1, 6

print(Solution().numBusesToDestination_1b(r, s, t))
