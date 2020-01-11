# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def add_node(val, root, queue):
    node = TreeNode(val)
    tree_node = queue[0]
    if tree_node.left == None:
        tree_node.left = node
        queue.append(tree_node.left)
        # print(myQueue, 'left')
    else:
        tree_node.right = node
        queue.append(tree_node.right)
        # print(myQueue, 'right')
        queue.pop(0)


def level_queue(root):
    if root == None:
        return
    queue = []
    node = root
    queue.append(node)
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)


class Solution:
    def levelOrder(self, root):
        pass


vals = [3, 9, 20, None, None, 15, 7]
root = TreeNode(vals[0])
queue = []
queue.append(root)
vals.pop(0)

for i in range(len(vals)):
    add_node(vals[i], root, queue)

# level_queue(root)

Solution().levelOrder(root)
