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

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
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
        if root:
            curr, nxt = root, root.left
        else:
            curr, nxt = root, None

        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:  # the gap between left node and right node
                curr.right.next = curr.next.left

            # update curr
            curr = curr.next
            if not curr:  # end of this row
                curr = nxt
                nxt = curr.left
        return root

