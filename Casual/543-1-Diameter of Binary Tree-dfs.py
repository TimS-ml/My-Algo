# https://leetcode-cn.com/problems/diameter-of-binary-tree/


# Definition of TreeNode
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Tree(object):
    def __init__(self):
        self.root = TreeNode(-1)
        self.istop = -1
        self.myQueue = []  # a buffer sequence

    def add(self, val):
        node = TreeNode(val)
        # if node is empty
        if self.istop == -1:
            self.root = node
            self.myQueue.append(self.root)
            print('Add', self.root.val, 'as top')
            self.istop += 1

        # if have node
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
                print('Add', treeNode.left, 'left of', treeNode)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)
                print('Add', treeNode.right, 'right of', treeNode)


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            print('left:', left, 'node:', node)
            right = dfs(node.right)
            print('right:', right, 'node:', node)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.ans


vals = [1, 2, 3, 4, 5]
tree = Tree()

for i in range(len(vals)):
    tree.add(vals[i])

print(Solution().diameterOfBinaryTree(tree.root))
