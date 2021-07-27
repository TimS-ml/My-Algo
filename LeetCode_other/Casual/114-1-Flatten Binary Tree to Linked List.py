# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# see 110 as a reference


class TreeNode(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.myQueue = []

    def add(self, val):
        node = TreeNode(val)

        # 如果树是空的，则对根节点赋值
        if self.root.val == -1:
            self.root = node
            self.myQueue.append(self.root)
            print(self.myQueue, self.root.val, 'top')

        # 如果有根节点
        else:
            treeNode = self.myQueue[0]  # 检查myQueue[0]的子树
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
                print(self.myQueue, self.root.val, 'left')
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # myQueue[0]节点左右都有了，pop掉
                print(self.myQueue, self.root.val, 'right')

    def level_queue(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right:
                return root

            if right is None:
                root.right = root.left
                root.left = None
                return left

            if not left:
                return right

            tmp = root.right
            root.right = root.left
            root.left = None
            left.right = tmp
            return right

        dfs(root)


vals1 = [-10, -3, 0, 5, 9]
tree = Tree()

for i in range(len(vals1)):
    tree.add(vals1[i])

# tree.level_queue(tree.root)

print(Solution().flatten(tree.root))
