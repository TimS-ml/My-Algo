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
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            # if it is the last node of this level, add it to the result
            if i == size - 1:
                result.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
