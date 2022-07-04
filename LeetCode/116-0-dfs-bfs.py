'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

# dfs
- full tree
- not only connect nodes belongs to same parent

# bfs
level order, keep track on prev and curr AT THE SAME LEVEL
'''

from collections import deque


# Definition for a Node.
class Node:

    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # traverse: ternary tree, dfs
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def traverse(node1, node2):
            if not node1 or not node2:
                return

            # pre-order
            node1.next = node2

            traverse(node1.left, node1.right)
            traverse(node2.left, node2.right)
            traverse(node1.right, node2.left)

        if not root:
            return root

        traverse(root.left, root.right)
        return root

    # bfs
    def connect_2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = deque([root])

        # Outer while loop which iterates over
        # each level
        while Q:

            # Note the size of the queue
            size = len(Q)

            # Iterate over all the nodes on the current level
            for i in range(size):

                # Pop a node from the front of the queue
                node = Q.popleft()

                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]

                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # Since the tree has now been modified, return the root node
        return root

    # Using previously established next pointers
    def connect_3(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root
