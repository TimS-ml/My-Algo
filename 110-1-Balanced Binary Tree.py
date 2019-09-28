# https://leetcode-cn.com/problems/balanced-binary-tree/


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
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(p):
            if not p:
                return 0
            left = dfs(p.left)
            right = dfs(p.right)
            if left==-1 or right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)

        if dfs(root)==-1:
            return False
        return True


vals1 = [3, 9, 20, None, None, 15, 7]
vals2 = [1, 2, 2, 3, 3, None, None, 4, 4]
tree = Tree()

for i in range(len(vals2)):
    tree.add(vals2[i])

# tree.level_queue(tree.root)  # root是最后建立出的树
print(Solution().isBalanced(tree.root))
