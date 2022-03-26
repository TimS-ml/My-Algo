'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

Pre-order:
- root + [pre-order left] + [pre-order right]

In-order:
- [in-order left] + root + [in-order right]

One thing to notice:
[pre-order left] != [in-order left]

Goal:
Construct and return the binary tree
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
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        preorder = deque(preorder)

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # find root note
            val = preorder.popleft()
            root = TreeNode(val)

            # split l-tree and r-tree based on root
            index = idx_map[val]

            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)
