'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class TreeNode(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # decomposition
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            # post-order
            # flatten
            left = node.left
            right = node.right

            # make left node as right
            node.left = None
            node.right = left

            # move right node
            p = node
            while p.right:
                p = p.right
            p.right = right

        dfs(root)

    # a not elegant solution
    def flatten_2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if not left and not right:
                return node

            if right is None:
                node.right = node.left
                node.left = None
                return left

            if not left:
                return right

            tmp = node.right
            node.right = node.left
            node.left = None
            left.right = tmp
            return right

        dfs(root)

    # traverse: if not in-place...
    def flatten_3(self, root: TreeNode):  # assume return allowed
        dummy = TreeNode(-1)
        p = dummy

        def traverse(node):
            if not node:
                return

            # pre-order
            p.right = TreeNode(node.val)
            p = p.right
            
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return dummy
