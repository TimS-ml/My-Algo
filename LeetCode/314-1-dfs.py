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
BFS solution: colTable[col].append(node.val)
dfs solution: colTable[col].append((row, node.val))
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
        colTable = defaultdict(list)
        visited = []  # Set to keep track of visited nodes

        def dfs(visited, node, row, col):
            if not node:
                return
            if node not in visited:
                visited.append(node)
                colTable[col].append((row, node.val))
                dfs(visited, node.left, row + 1, col - 1)
                dfs(visited, node.right, row + 1, col + 1)

        dfs(visited, root, 0, 0)

        ans = []
        for col in sorted(colTable.keys()):
            # the order of val appended are different
            # that's why dfs need sort but bfs doesn't
            colTable[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in colTable[col]]
            ans.append(colVals)

        return ans

    def verticalOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        colTable = defaultdict(list)
        min_col = max_col = 0

        def dfs(node, row, col):
            if node is not None:
                nonlocal min_col, max_col
                colTable[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                # preorder dfs
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        # order by col and sort by row
        ans = []
        for col in range(min_col, max_col + 1):
            # the order of val appended are different
            # that's why dfs need sort but bfs doesn't
            colTable[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in colTable[col]]
            ans.append(colVals)

        return ans
