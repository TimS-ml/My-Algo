'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # convert into a graph
    def distanceK(self, root, target, K):
        conn = collections.defaultdict(list)
        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)

            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        # the initial parent node of the root is None
        connect(None, root)

        # start the breadth-first search from the target, hence the starting level is 0
        q = [target.val]
        seen = set(q)
        # all nodes at (k-1)th level must also be K steps away from the target node
        for _ in range(K):
            # expand the list comprehension to strip away the complexity
            new_level = []
            for q_node_val in q:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            q = new_level  # update q to current level
            # add all the values in bfs into seen
            seen |= set(q)
        return q

        
    # the dfs solution
    # in graph traversal, use 'seen' or 'visited' to track the traversal never goes back
    def distanceK_2(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        conn = collections.defaultdict(list)
        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)

            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        connect(None, root)
       
        visited = set()
        ans = []

        def dfs(node, distance):
            if node in visited:
                return
            
            visited.add(node)
            
            if distance == K:
                ans.append(node)
            elif distance < K:
                for n in conn[node]:
                    dfs(n, distance + 1)
        
        dfs(target.val, 0)
        return ans
