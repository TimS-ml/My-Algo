'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
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

        # if tree is empty, assign vale to root
        if self.root.val == 0:
            self.root = node
            self.myQueue.append(self.root)
            # print(self.myQueue, self.root.val, 'top')

        else:
            treeNode = self.myQueue[0]  # examine myQueue[0]'s child-tree
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
                # print(self.myQueue, self.root.val, 'left')
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # myQueue[0] has l and r node, pop
                # print(self.myQueue, self.root.val, 'right')

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        return ans


li = [1, 2, 3]

tree = Tree()
for i in range(len(li)):
    tree.add(li[i])

# tree.level_queue(tree.root)

# print(Solution().xxx(tree.root))
