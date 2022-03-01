'''
# Code Explain:
N is the number of nodes in the tree
- Time complexity: O(N)
- Space complexity: O(N)

- dfs or bfs, save the value
- sum the value between low and high
- return sum

- include low and high
- low <= high

!!! use the info of binary search tree
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # dfs
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0  # or you can use self.s
        def dfs(node):
            nonlocal s
            if node:
                if low <= node.val <= high:
                    s += node.val
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return s

    # a better dfs
    def rangeSumBST_2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:  # use the info of binary search tree
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
    
    # bfs
    def rangeSumBST_3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if node:
                if low <= node.val <= high:
                    s += node.val
                if low < node.val:  # use the info of binary search tree
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return s

