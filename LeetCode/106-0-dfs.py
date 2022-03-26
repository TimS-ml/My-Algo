'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

According to the characteristics of in-order traversal and post-order traversal, we analyze the restoration process of the tree
- Find the root node (the last element) in the post-order traversal sequence
- Find the position of the root node in the in-order traversal sequence
    - The in-order traversal sequence is divided into a left subtree and a right subtree
- Determine the left and right boundary positions of the left and right subtrees in the in-order array and post-order arrays according to the position of the root node
- Recursively construct left and right subtrees
- Return to the end of the root node

'''

from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}

        def build(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None

            # find root note in postorder
            # since postorder = [l, r, root], pop returns root of r
            # that's the reason we put root.right at first
            val = postorder.pop()
            root = TreeNode(val)

            # inorder index
            # split l-tree and r-tree based on root
            index = inorder_idx_map[val]

            root.right = build(index + 1, inorder_right)
            root.left = build(inorder_left, index - 1)
            return root

        return build(0, len(inorder) - 1)

