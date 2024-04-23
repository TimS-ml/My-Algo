'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        N = set(nodes)  # a set of TreeNode

        def helper(node):
            if not node:
                return None

            # terminate, case 2, find 1 node
            if node in N:
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
