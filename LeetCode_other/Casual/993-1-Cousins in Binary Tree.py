# https://leetcode-cn.com/problems/cousins-in-binary-tree/


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

        # 如果树是空的, 则对根节点赋值
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
                self.myQueue.pop(0)  # myQueue[0]节点左右都有了, pop掉
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
    def isCousins(self, root, x, y):
        # if len(root) <= 4:
        #     return False
        # else:
        #     for i in range(len(root)):
        #         x -= 2**i
        #         y -= 2**i
        #         if x <= 0:
        #             layer_x = i
        #         if y <= 0:
        #             layer_y = i
        #         if x <= 0 and y <= 0:
        #             break
        # if layer_x == layer_y:
        #     return True
        return False


list1 = [1, 2, 3, 4]
x1 = 4
y1 = 3

list2 = [1, 2, 3, None, 4, None, 5]
x2 = 5
y2 = 4

tree = Tree()
for i in range(len(list1)):
    tree.add(list1[i])

# tree.level_queue(tree.root)

print(Solution().isCousins(list1, x1, y1))
