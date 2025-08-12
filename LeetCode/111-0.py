'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_depth = float('inf')
        self.curr_depth = 0

    def minDepth_dfs(self, root: TreeNode) -> int:
        if root is None: return 0
        self.traverse(root)
        return self.min_depth
    
    def traverse(self, root: TreeNode) -> None:
        if root is None: return 0
        
        self.curr_depth += 1

        if root.left is None and root.right is None:
            self.min_depth = min(self.min_depth, self.curr_depth)

        self.traverse(root.left)
        self.traverse(root.right)

        self.curr_depth -= 1

    def minDepth_bfs(self, root: TreeNode) -> int:
        if root is None: return 0
        
        q = deque([root])
        depth = 1

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()

                # bfs shortest leaf found!
                if cur.left is None and cur.right is None:
                    return depth

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)

            depth += 1

        return depth

