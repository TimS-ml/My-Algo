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
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        colTable = defaultdict(list)
        queue = deque([(root, 0)])  # the <node, col> pattern

        while queue:
            node, col = queue.popleft()

            if node is not None:
                # if you are using normal dict, you may need to init first
                colTable[col].append(node.val)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        # colTable.keys() is the col location
        # since it's bfs, upper level nodes will append first in same col
        return [colTable[x] for x in sorted(colTable.keys())]

    # this is smart: based on the fact that you already know the
    # target `col key` is in ascending order
    def verticalOrder_2(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        colTable = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is not None:
                colTable[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [colTable[x] for x in range(min_col, max_col + 1)]
