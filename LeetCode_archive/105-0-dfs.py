'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

Pre-order:
- root + [pre-order left] + [pre-order right]

In-order:
- [in-order left] + root + [in-order right]

Goal:
- Construct and return the binary tree
- How to find root node?
    - pre-order start is the root
    - left size: len 0 ~ in-order root
    - len pre-order left = len in-order left
    - Note: [pre-order left] != [in-order left]
'''

from typing import List
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # since number is unique, it's OK to use idx hash map
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        preorder = deque(preorder)

        def build(inStart, inEnd):
            if inStart > inEnd:
                return None

            # find root note
            # this is tricky, since we don't have idx of pre-order
            root_val = preorder.popleft()
            root = TreeNode(root_val)

            # split l-tree and r-tree based on root
            inorderRootIdx = inorder_idx_map[root_val]

            # !!! left first !!!
            # !!! does not include inorderRootIdx !!!
            root.left = build(inStart, inorderRootIdx - 1)
            root.right = build(inorderRootIdx + 1, inEnd)
            return root

        return build(0, len(inorder) - 1)

    def buildTree_2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}

        def build(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd:
                return None

            rootVal = preorder[preStart]

            # find in in-order in range(inStart, inEnd+1)
            # be aware of this edge case
            # if use hash map, then inStart, inEnd are not necessary...
            inorderRootIdx = inorder_idx_map[rootVal]

            leftSize = inorderRootIdx - inStart

            root = TreeNode(rootVal)
            # idx = inStart+leftSize
            root.left = build(preStart + 1, preStart + leftSize,
                              inStart, inStart + leftSize - 1)
            root.right = build(preStart + leftSize + 1, preEnd,
                               inStart + leftSize + 1, inEnd)
            return root

        return build(0, len(preorder)-1,
                     0, len(inorder)-1)
