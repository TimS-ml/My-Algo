'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

A asc order traversal of BST: in-order
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        ans = float('inf')
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            nonlocal curr
            curr += 1
            if curr == k:
                nonlocal ans
                ans = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return ans 
