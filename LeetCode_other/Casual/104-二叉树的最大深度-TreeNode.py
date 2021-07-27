# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

# 题目整理
# https://www.hrwhisper.me/leetcode-tree/
# 代码补全
# http://www.10qianwan.com/articledetail/116092.html

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


root = TreeNode([3, 9, 20, None, None, 15, 7])
print(Solution().maxDepth(root))
