'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

from __future__ import print_function
from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
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


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
