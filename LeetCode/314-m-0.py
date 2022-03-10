'''
- if BFS: Need something to track vertical order
- if DFS: track vertical and horizontal order both
- The order in the same vertical col matters
    - use BFS
- Relationship of vertical columns
    - left and right
'''

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = defaultdict([[root, 0]])
        col = {}
        while queue:
            node, colnumber = queue.popleft()
            # how to get this
            col[colnumber] = node.val
            queue.append([node.left, colnumber-1],
                          [node.right, colnumber+1])
            
        ans = []
        mincol, maxcol = min(col.keys()), max(col.keys())
        for c in range(mincol, maxcol+1):
            ans.append(col[c])

        return ans
