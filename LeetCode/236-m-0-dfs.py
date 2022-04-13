'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

case 1
p in lca.l and q in lca.r

case 2
q in p.l or p.r
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return None

            # terminate, case 2, find 1 node
            if node.val == p.val or node.val == q.val:
                return node

            l = helper(node.left)
            r = helper(node.right)

            # case 1
            if l and r:
                return node
            
            # case 2
            if l:
                return l
            else:
                return r
        
        return helper(root)
