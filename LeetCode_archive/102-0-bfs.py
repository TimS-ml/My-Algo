'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = [[root.val]]
        queue = deque([root])
        while queue:
            levelList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    levelList.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    levelList.append(node.right.val)
                    queue.append(node.right)
            if levelList:
                ans.append(levelList)
        return ans

