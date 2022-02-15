'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


BFS uses a queue to save the path sum when traversing to each node
If the node happens to be a leaf node, and the path sum is exactly equal to sum, then it means that you have found the ans
'''

import collections


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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        que_node = collections.deque([root])
        que_val = collections.deque([root.val])

        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == targetSum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)

        return False

    def hasPathSum_dfs(self, root: TreeNode, targetSum: int) -> bool:
        # if not root:
        #     return False
        # if not root.left and not root.right:
        #     return sum == root.val
        # return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
        #     root.right, sum - root.val)
        def dfs(node, s):
            if not node:
                return False
            if not node.left and not node.right:
                return s == node.val
            return dfs(node.left, s - node.val) or dfs(node.right,
                                                       s - node.val)

        return dfs(root, targetSum)


li = [1, 2, 3]

tree = Tree()
for i in range(len(li)):
    tree.add(li[i])

# tree.level_queue(tree.root)

#  print(Solution().xxx(tree.root))
