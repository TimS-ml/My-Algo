# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        h_l, h_r = 0, 0
        # 计算当前节点左子树的最大高度
        curRoot = root
        while curRoot.left:
            h_l += 1
            curRoot = curRoot.left
        # 计算当前节点右子树的最大高度
        curRoot = root
        if curRoot.right:
            h_r += 1
            curRoot = curRoot.right
            while curRoot.left:
                h_r += 1
                curRoot = curRoot.left
        
        # 左右子树最大高度相同，说明左子树为满二叉树，在右子树继续递归求解     
        if h_l == h_r:
            sumNodes_r = self.countNodes(root.right)
            sumNodes_l = 2**h_l - 1
        # 左子树高度更高，说明右子树为满二叉树，在左子树继续递归求解   
        if h_l == h_r + 1:
            sumNodes_l = self.countNodes(root.left)
            sumNodes_r = 2**h_r - 1
         
        # 返回左子节点个数+右子节点个数+当前根节点   
        return sumNodes_l + sumNodes_r + 1

