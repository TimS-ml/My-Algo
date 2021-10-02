'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:

left, right, root

recursion vs stack:
the difference is that a stack is implicitly maintained during recursion
and we need to explicitly simulate this stack when iteration, and the rest of the implementation and details are the same
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

        # 如果树是空的, 则对根节点赋值
        if self.root.val == 0:
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
    def postorderTraversal_recursion(self, root: TreeNode) -> List[int]:
        ans = []

        def recursion(root):
            if not root:
                return
            recursion(root.left)
            recursion(root.right)
            ans.append(root.val)

        recursion(root)
        return ans

    def postorderTraversal_stack(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return ans


li = [1, 2, 3]
#  li = [-10, 9, 20, None, None, 15, 7]

tree = Tree()
for i in range(len(li)):
    tree.add(li[i])

#  tree.level_queue(tree.root)

print(Solution().postorderTraversal(tree.root))
