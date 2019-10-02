# https://leetcode-cn.com/problems/symmetric-tree/


# 此处有改动，多加了left和right，方便传递参数
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root) -> bool:
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)


tree1 = TreeNode(1, (2, 3, 4), (2, 3, 4))
tree2 = TreeNode(1, (2, 3, 4), (2, 4, 3))
tree3 = TreeNode(1, (2, 3, (4, 3)), (2, (4, None, 3), 3))
print(Solution().isSymmetric(tree1))
# print(TreeNode.left)
