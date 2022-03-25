'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
    If the tree is balanced, it'd be O(logN)
'''


# Definition of TreeNode
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # post-order: fast
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.ans
    
    # pre-order: slow, time O(N^2), just for demonstration
    def diameterOfBinaryTree_2(self, root):
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


vals = [1, 2, 3, 4, 5]
tree = Tree()

for i in range(len(vals)):
    tree.add(vals[i])

print(Solution().diameterOfBinaryTree(tree.root))
