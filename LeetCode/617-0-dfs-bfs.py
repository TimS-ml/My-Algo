'''
# Code Explain:
- Time complexity: O(min(m, n))
- Space complexity: O(min(m, n))

# Pros and Cons and Notation:

The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

- how to align the tree
- inplace or not
- a, b are both empty
- a, b one is empty
- a, b are both not empty

dfs
[1] Base State
[2] State Transfer Equation
[3] Backtrack senario
[4] Initialize Conditions
[5] Terminate Conditions
'''

from typing import List
from collections import deque


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
    # dfs
    def mergeTrees_dfs(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        # NoneType + number will rise error
        v1 = root1.val if root1.val else 0
        v2 = root2.val if root2.val else 0
        ans = TreeNode(v1 + v2)
        # ans = TreeNode(root1.val + root2.val)
        ans.left = self.mergeTrees_dfs(root1.left, root2.left)
        ans.right = self.mergeTrees_dfs(root1.right, root2.right)
        return ans

    # bfs
    def mergeTrees_bfs(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        v1 = root1.val if root1.val else 0
        v2 = root2.val if root2.val else 0
        ans = TreeNode(v1 + v2)
        queue = deque([ans])
        queue1 = deque([root1])
        queue2 = deque([root2])

        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            left1, left2 = node1.left, node2.left
            right1, right2 = node1.right, node2.right

            if left1 or left2:
                if left1 and left2:
                    v1 = left1.val if left1.val else 0
                    v2 = left2.val if left2.val else 0
                    left = TreeNode(v1 + v2)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:
                if right1 and right2:
                    v1 = right1.val if right1.val else 0
                    v2 = right2.val if right2.val else 0
                    right = TreeNode(v1 + v2)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2
        return ans


root1 = [1, 3, 2, 5]
root2 = [2, 1, 3, None, 4, None, 7]

tree1 = Tree()
for i in range(len(root1)):
    tree1.add(root1[i])

tree2 = Tree()
for i in range(len(root2)):
    tree2.add(root2[i])

# merged = Solution().mergeTrees_dfs(tree1.root, tree2.root)
merged = Solution().mergeTrees_bfs(tree1.root, tree2.root)
ans = Tree()
ans.level_queue(merged)
