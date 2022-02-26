'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

What do I need:
<x, y> of each point

BFS with row alignment
Create a stack (?) tracking
root.left  = <x_root.x - 1, x_root.y - 1>
root.right = <x_root.x + 1, x_root.y - 1>
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
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])  # the <node, column> pattern

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]

