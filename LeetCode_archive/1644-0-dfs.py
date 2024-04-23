'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        def helper(node):
            nonlocal findp, findq
            if not node:
                return None

            # DON'T terminate when node == p or node == q
            # instead, search whole tree
            r = helper(node.right)
            l = helper(node.left)

            # case: node is one of the target
            if node == p:
                findp = True
                return node
            if node == q:
                findq = True
                return node

            # case: find both lca
            if l and r:
                return node

            # case: only find one target in one branch
            if l:
                return l
            elif r:
                return r
            else:
                return None

        findp, findq = False, False
        ans = helper(root)

        if findp and findq:
            return ans
        return None

