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
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        res = []
        queue = []

        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            while size:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            # 执行操作
            # res.append(list(temp))
            res.insert(0, list(temp))
        return res
