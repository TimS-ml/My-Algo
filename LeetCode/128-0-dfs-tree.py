'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
Value:
- empty node = 0
- non-leaf node = node.val + children's val
- leaf node = node.val

Recursion:
- Base state
- State transfer
- Init / Terminate Condiction

def dfs(root):
    if not root: return
    dfs(root.left)
    dfs(root.right)
'''


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
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # choose this children only if it's contribute > 0
            leftGain = max(dfs(node.left), 0)
            rightGain = max(dfs(node.right), 0)

            # current answer
            priceNewpath = node.val + leftGain + rightGain

            # update answer
            self.maxSum = max(self.maxSum, priceNewpath)

            # max contribute of this node
            return node.val + max(leftGain, rightGain)

        dfs(root)
        return self.maxSum


li = [1, 2, 3]
#  li = [-10, 9, 20, None, None, 15, 7]

tree = Tree()
for i in range(len(li)):
    tree.add(li[i])

#  tree.level_queue(tree.root)

print(Solution().maxPathSum(tree))
