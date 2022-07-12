'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:
    def find_maximum_path_sum(self, root):
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

