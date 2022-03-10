'''
# Code Explain:
N is number of nodes
- Time complexity: O(NlogN)
- Space complexity: O(N)

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
                # if you are using normal dict, you may need to init first
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        # columnTable.keys() is the column location
        # since it's bfs, upper level nodes will append first in same col
        return [columnTable[x] for x in sorted(columnTable.keys())]

    # this is smart: based on the fact that you already know the
    # target `col key` is in ascending order
    def verticalOrder_2(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]
