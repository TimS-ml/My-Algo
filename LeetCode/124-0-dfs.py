'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(H)
N = number of nodes
H = tree height, best: logN, worse: N (skewed tree)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = -float('INF')
        
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            
            lMaxSum = max(0, helper(node.left))
            rMaxSum = max(0, helper(node.right))
            
            # post order
            # treat current node as root
            pathMaxSum = node.val + lMaxSum + rMaxSum
            ans = max(ans, pathMaxSum)
            
            # return number as a non-root l/r branch
            return max(lMaxSum, rMaxSum) + node.val
        
        helper(root)
        return ans
