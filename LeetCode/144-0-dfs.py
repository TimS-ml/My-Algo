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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ans

    def preorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            # right child is pushed first so that left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
