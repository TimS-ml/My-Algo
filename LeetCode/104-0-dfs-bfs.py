'''
# Code Explain:
dfs
- Time complexity: O(N)
- Space complexity: O(height of tree)

bfs
- Time complexity: O(N)
- Space complexity: O(width of tree)
'''

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth_dfs(self, root) -> int:
        ans = 0
        def dfs(node, depth):  # return maxLen
            if not node:
                nonlocal ans
                ans = max(ans, depth)
                return
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)
            depth -= 1
            return
        
        dfs(root, 0)
        return ans

    def maxDepth_dfs_2(self, root) -> int:
        def dfs(node):  # return maxLen
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1

        return dfs(root)

    def maxDepth_bfs(self, root) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = 0  # depth
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
        return ans


root = TreeNode([3, 9, 20, None, None, 15, 7])
print(Solution().maxDepth(root))
