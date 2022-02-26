'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        if not root:
            return [0]
        queue = [root]
        res = []

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
            res.append(sum(temp) / float(len(temp)))
        return res
