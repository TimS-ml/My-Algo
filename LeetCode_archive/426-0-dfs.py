'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            # the 'last' node is the node that we create double link with curr node
            # the 'first' node is the node that we create circle after recursion
            nonlocal last, first
            if node:
                # left
                helper(node.left)

                # middle node
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                    last = node
                else:
                    # init, only run once
                    # keep the smallest node
                    # to close DLL later on
                    first = node
                    last = node

                # right
                helper(node.right)

        if not root:
            return None

        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first

    # a interesting solution... post order
    def treeToDoublyList_2(self, node: 'Node') -> 'Node':
        def helper(node):
            if not node:
                return None

            # turn left and right to cyc List
            lHead = helper(node.left)
            rHead = helper(node.right)

            # put node in the middle of 2 cyc list l and r
            if lHead:
                lTail = lHead.left  # that's the reason why you need a cyc list
                node.left = lTail
                lTail.right = node
            else:
                lTail = lHead = node

            if rHead:
                rTail = rHead.left
                node.right = rHead
                rHead.left = node
            else:
                rTail = rHead = node

            lHead.left = rTail
            rTail.right = lHead

            return lHead

        return helper(root)

