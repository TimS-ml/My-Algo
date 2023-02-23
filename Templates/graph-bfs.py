from collections import defaultdict


class Solution:
    # lc 815, depth from S to T
    def graph_depth(self, routes, S, T):
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

