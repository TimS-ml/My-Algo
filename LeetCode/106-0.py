'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)



According to the characteristics of in-order traversal and post-order traversal, we analyze the restoration process of the tree
- Find the root node (the last element) in the post-order traversal sequence
- Find the position of the root node in the in-order traversal sequence
    - The in-order traversal sequence is divided into a left subtree and a right subtree
- Determine the left and right boundary positions of the left and right subtrees in the in-order array and post-order arrays according to the position of the root node
- Recursively construct left and right subtrees
- Return to the end of the root node

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # find root note in postorder
            # since postorder = [l, r, root], pop returns root of r
            # that's the reason we put root.right at first
            val = postorder.pop()
            root = TreeNode(val)

            # inorder index
            # split l-tree and r-tree based on root
            index = idx_map[val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        return helper(0, len(inorder) - 1)


li = [1, 2, 3]

tree = Tree()
for i in range(len(li)):
    tree.add(li[i])

# tree.level_queue(tree.root)

# print(Solution().xxx(tree.root))
