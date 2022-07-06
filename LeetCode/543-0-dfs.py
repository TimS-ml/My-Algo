'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
    If the tree is balanced, it'd be O(logN)

check lc 104
'''


# Definition of TreeNode
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # pre-order: slow, time O(N^2)
    # lc 104 sol 1
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return

            # pre-order: to get depth,
            # we have to relay on help function
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            self.ans = max(self.ans, left + right)
            
            dfs(node.left)
            dfs(node.right)

        def maxDepth(node):
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)

            # post-order location: empty
            return max(left, right) + 1

        dfs(root)
        return self.ans

    # post-order + split sub-problems
    # lc 104 sol 2
    def diameterOfBinaryTree_2(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # post-order
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1  # remember to +1

        dfs(root)
        return self.ans

