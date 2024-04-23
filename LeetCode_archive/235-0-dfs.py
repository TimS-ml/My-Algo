'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

def lowestCommonAncestor(self, root, p, q):
    v1 = min(p.val, q.val)
    v2 = max(p.val, q.val)
    def dfs(node):
        # !!! don't forgot!!!
        if not node:
            return None

        # !!!!! return !!!!!
        if v2 < node.val:
            return dfs(node.left)

        if v1 > node.val:
            return dfs(node.right)

        return node
    return dfs(root)
