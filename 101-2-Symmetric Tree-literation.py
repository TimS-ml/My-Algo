# https://leetcode-cn.com/problems/symmetric-tree/


# 此处有改动，多加了left和right，方便传递参数
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root) -> bool:
        queue = [root]

        while (queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            queue = next_queue

        return True


tree1 = TreeNode(1, (2, 3, 4), (2, 3, 4))
tree2 = TreeNode(1, (2, 3, 4), (2, 4, 3))
tree3 = TreeNode(1, (2, 3, (4, 3)), (2, (4, None, 3), 3))
print(Solution().isSymmetric(tree1))
