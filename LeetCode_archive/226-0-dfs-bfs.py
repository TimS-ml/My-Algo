'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Invert node.left and node.right for every node
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # traverse
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return

            # pre-order
            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)

            # post-order is also OK
            # node.left, node.right = node.right, node.left

        dfs(root)
        return root

    # decomposition
    def invertTree_2(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if not node:
                return

            left = invert(node.left)
            right = invert(node.right)

            node.left = right
            node.right = left

            return node

        return invert(root)

    # traverse, iter version
    def invertTree_bfs(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # print(node.val)
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
