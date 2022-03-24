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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        def helper(node, level):
            # start the current level
            if len(ans) == level:
                ans.append([])

            # append the current node value
            ans[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return ans[::-1]
