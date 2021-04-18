# As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.

# The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present or False if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.

# Finish the route_exists method so that it returns True if the destination is reachable or False if it is not. The from_row and from_column parameters are the starting row and column in the map_matrix. 
# The to_row and to_column are the destination row and column in the map_matrix. The map_matrix parameter is the above mentioned matrix produced from the map.

from collections import deque

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    """ This is queue version
        If you want to test with stack, follow steps.
        1. In solution with stack, no need to deque and enough to python list. ([])
        2. variable change q to s (conventionally) in lines 14, 15, 19.
        3. q.popleft() to s.pop() in line 22.
        4. q.append(direction) to s.append(direction) in line 40.
    """

    size = (len(map_matrix), len(map_matrix[0]))
    q = deque()
    q.append((from_row, from_column))
    visited = [[False] * size[1] for _ in range(size[0])]

    while True:
        if len(q) == 0:
            return False

        current = q.popleft()
        if current[0] == to_row and current[1] == to_column:
            return True
        
        visited[current[0]][current[1]] = True
        up = (current[0] - 1, current[1])
        down = (current[0] + 1, current[1])
        left = (current[0], current[1] - 1)
        right = (current[0], current[1] + 1)

        next_candidates = (up, right, down, left)
        for direction in next_candidates:
            if 0 <= direction[0] and direction[0] < size[0] \
                and 0 <= direction[1] and direction[1] < size[1]:

                if map_matrix[direction[0]][direction[1]] and \
                    not visited[direction[0]][direction[1]]:

                    q.append(direction)

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
