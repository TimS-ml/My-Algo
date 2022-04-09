'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

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
    # bfs
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colTable = defaultdict(list)
        queue = deque([(root, 0, 0)])  # the <node, row, col> pattern

        while queue:
            node, row, col = queue.popleft()

            if node is not None:
                # if you are using normal dict, you may need to init first
                colTable[col].append((row, node.val))

                queue.append((node.left, 
                              row + 1, col - 1))
                queue.append((node.right, 
                              row + 1, col + 1))

        ans = []
        # return [colTable[x] for x in sorted(colTable.keys())]
        for col in sorted(colTable.keys()):
            colTable[col].sort(key=lambda x:[x[0], x[1]])  # this line is different than 314
            colVals = [val for row, val in colTable[col]]
            ans.append(colVals)
        return ans

    # dfs
    def verticalTraversal_2(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            colTable[col].sort(key=lambda x:[x[0], x[1]])  # this line is different than 314
            colVals = [val for row, val in colTable[col]]
            ans.append(colVals)

        return ans
