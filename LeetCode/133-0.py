'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

dfs + visited
'''

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    # dfs
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        def dfs(node):
            if not node:
                return node

            # If the node was already visited before.
            # Return the clone from the visited dictionary.
            if node in visited:
                return visited[node]

            # Create a clone for the given node.
            # Note that we don't have cloned neighbors as of now, hence [].
            clone_node = Node(node.val, [])

            # The key is original node and value being the clone node.
            visited[node] = clone_node

            # !!! Iterate through the neighbors to generate their clones
            # and prepare a list of cloned neighbors to be added to the cloned node.
            if node.neighbors:
                clone_node.neighbors = [dfs(n) for n in node.neighbors]

            return clone_node

        return dfs(node)

    # bfs
    def cloneGraph_2(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)

                # !!! Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
