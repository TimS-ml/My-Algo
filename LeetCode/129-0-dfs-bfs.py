'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # dfs
    def sumNumbers(self, root: TreeNode):
        def preorder(node, curr_number):
            nonlocal ans
            if node:
                curr_number = curr_number * 10 + node.val
                # if it's a leaf, update root-to-leaf sum
                if not (node.left or node.right):
                    ans += curr_number
                    
                preorder(node.left, curr_number)
                preorder(node.right, curr_number) 
        
        ans = 0
        preorder(root, 0)
        return ans

    def sumNumbers_2(self, root: TreeNode):
        def preorder(node):
            nonlocal ans
            path.append(str(node.val))
            # if it's a leaf, update root-to-leaf sum
            if not (node.left or node.right):
                ans += int(''.join(path))
                
            # remember to add a post order pop
            if node.left:
                preorder(node.left)
                path.pop()
            
            if node.right:
                preorder(node.right) 
                path.pop()
        
        path = []
        ans = 0
        preorder(root)
        return ans
