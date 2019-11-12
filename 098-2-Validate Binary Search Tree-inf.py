# https://leetcode-cn.com/problems/validate-binary-search-tree/
# TypeError: '<=' not supported between instances of 'NoneType' and 'int'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def addNode(val, root, myQueue):
    node = TreeNode(val)
    treeNode = myQueue[0]
    if treeNode.left == None:
        treeNode.left = node
        myQueue.append(treeNode.left)
        # print(myQueue, 'left')
    else:
        treeNode.right = node
        myQueue.append(treeNode.right)
        # print(myQueue, 'right')
        myQueue.pop(0)


def level_queue(root):
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
    def isValidBST(self, root: TreeNode) -> bool:
        prev = -float("inf")  # 正无穷
        stack = [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]:
                continue
            if p[0] == 0:
                if p[1].val <= prev:
                    return False
                prev = p[1].val
            else:
                stack.append((1, p[1].right))
                stack.append((0, p[1]))
                stack.append((1, p[1].left))
        return True


# vals = [5, 1, 4, None, None, 3, 6]
vals = [10, 5, 15, None, None, 6, 20]
root = TreeNode(vals[0])
myQueue = []
myQueue.append(root)
vals.pop(0)

for i in range(len(vals)):
    addNode(vals[i], root, myQueue)

# level_queue(root)

print(Solution().isValidBST(root))
