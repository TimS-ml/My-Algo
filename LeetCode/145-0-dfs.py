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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        dfs(root)
        return ans

    def postorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        pre = None
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                peak = stack[-1]
                if peak.right and peak.right != pre:
                    node = peak.right
                else:
                    stack.pop()
                    ans.append(peak.val)
                    pre = peak
        return ans
