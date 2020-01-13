# Version 1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def listToTreeNode(inputValues):
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            # leftNumber = int(item)
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)
            print('Add', node.left.val, 'left of', node.val)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            # rightNumber = int(item)
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
            print('Add', node.right.val, 'right of', node.val)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while queue[current]:
        node = queue[current]
        # print(node.val)
        current = current + 1

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


# line = [4,2,7,1,3,6,9]
line = [3, 9, 20, None, None, 15, 7]
root = listToTreeNode(line)
ans = Solution().invertTree(root)
out = treeNodeToString(ans)
print(out)
