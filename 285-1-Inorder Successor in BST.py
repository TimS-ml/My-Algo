# https://leetcode-cn.com/problems/inorder-successor-in-bst/


# Definition for a binary tree node.
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
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root and p:
            flag = False
            stack = [(1, root)]
            while stack:
                q = stack.pop()
                if not q[1]:
                    continue
                if q[0] == 0:
                    if flag:
                        return q[1]
                    if q[1] == p:
                        flag = True
                else:
                    stack.extend([(1, q[1].right), (0, q[1]), (1, q[1].left)])
        return None


vals = [5, 3, 6, 2, 4, None, None, 1]
p = 6
tree = Tree()

for i in range(len(vals)):
    tree.add(vals[i])

# tree.level_queue(tree.root)  # root是最后建立出的树
print(Solution().inorderSuccessor(tree.root, p))
