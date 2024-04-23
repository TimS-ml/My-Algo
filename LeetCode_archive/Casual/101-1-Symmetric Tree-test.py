# https://leetcode-cn.com/problems/symmetric-tree/


# 此处有改动, 多加了left和right, 方便传递参数
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        def isSymmetriclr(left, right):
            if not (left or right):
                return True
            if (left == None and right) or (left and right == None):
                return False
            if left.val != right.val:
                return False
            if not isSymmetriclr(left.left, right.right):
                return False
            if not isSymmetriclr(left.right, right.left):
                return False
            return True

        while root:
            return isSymmetriclr(root.left, root.right)


tree = TreeNode(1, (2, 3, 4), (2, 3, 4))

print(Solution().isSymmetric(tree))
