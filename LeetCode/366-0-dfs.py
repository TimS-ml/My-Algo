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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def maxDepth(node):
            if not node:
                return 0
            
            # get max depth of tree
            h = max(maxDepth(node.left), maxDepth(node.right)) + 1
            
            # post order
            nonlocal ans
            if len(ans) < h:
                ans.append([])
            
            ans[h-1].append(node.val)
            return h
            
        ans = []
        maxDepth(root)
        return ans
