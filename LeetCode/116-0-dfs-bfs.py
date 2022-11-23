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

        # traverse gap
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

        Q = deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()

                # This check ensures we don't establish
                # next pointers beyond the end of a level
                if i < size - 1:
                    node.next = Q[0]  # Q[0] is the next node

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return root

    # Using previously established next pointers
    # iter version of sol 1
    def connect_3(self, root: 'Node') -> 'Node':

        if not root:
            return root

        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:
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
