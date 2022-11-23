'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        return ans

    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        ans = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans.append(root.val)
                root = root.right

        return ans
