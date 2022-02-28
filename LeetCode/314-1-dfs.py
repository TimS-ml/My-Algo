'''
# Code Explain:
N is number of no
- Time complexity: O(NlogN)
- Space complexity: O(N)

What do I need:
<x, y> of each point

This is dfs, the node order inside dict are different
so we need to keep in track of both row and col:
Modified based on BFS: 
BFS solution: columnTable[column].append(node.val)
dfs solution: columnTable[column].append((row, node.val))
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
        # why this is faster? Maybe because the min max comparison?
        columnTable = defaultdict(list)
        visited = []  # Set to keep track of visited nodes

        def dfs(visited, node, row, column):
            if not node:
                return
            if node not in visited:
                visited.append(node)
                columnTable[column].append((row, node.val))
                dfs(visited, node.left, row + 1, column - 1)
                dfs(visited, node.right, row + 1, column + 1)

        dfs(visited, root, 0, 0)

        ans = []
        for col in sorted(columnTable.keys()):
            columnTable[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in columnTable[col]]
            ans.append(colVals)

        return ans

    def verticalOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def dfs(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder dfs
                dfs(node.left, row + 1, column - 1)
                dfs(node.right, row + 1, column + 1)

        dfs(root, 0, 0)

        # order by column and sort by row
        ans = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in columnTable[col]]
            ans.append(colVals)

        return ans
