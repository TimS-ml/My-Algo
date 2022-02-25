'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

What do I need:
<column, row> of each point

BFS with row alignment
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
