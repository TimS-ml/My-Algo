# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 题目理解出了一些问题“节点的右子树只包含大于当前节点的数”
# 包括右子树的左树


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
    def isValidBST(self, root) -> bool:
        if root == None:
            return True
        myQueue = []
        node = root
        myQueue.append(node)
        # print(myQueue, 'start')
        while myQueue:
            node = myQueue.pop(0)
            # print(node.val)
            if node.left != None:
                if node.left.val != None and node.left.val <= node.val:
                    print('left', node.left.val, node.val)
                    myQueue.append(node.left)
                elif node.left.val != None and node.left.val > node.val:
                    print('left-f', node.left.val, node.val)
                    return False

            if node.right != None:
                if node.right.val != None and node.right.val >= node.val:
                    print('right', node.right.val, node.val)
                    myQueue.append(node.right)
                elif node.right.val != None and node.right.val < node.val:
                    print('right-f', node.right.val, node.val)
                    return False
            # print(myQueue, node.val)
        return True


# vals = [5, 1, 5, None, None, 3, 6]
# vals = [1, 1]
vals = [10, 5, 15, None, None, 6, 20]  # 应该是右子树的6，实际应该在10-15之间
root = TreeNode(vals[0])
myQueue = []
myQueue.append(root)
vals.pop(0)

for i in range(len(vals)):
    addNode(vals[i], root, myQueue)

# level_queue(root)

print(Solution().isValidBST(root))
