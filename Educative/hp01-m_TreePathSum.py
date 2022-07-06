'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, s):
    if root is None:
        return False

    def dfs(node, remain):
        if not node.left and not node.right:
            return remain == node.val
        # the terminate case not this:
        # if not node:
        #     return remain == 0
        if node.left:
            left = dfs(node.left, remain - node.val)
        else:
            left = False
        if node.right:
            right = dfs(node.right, remain - node.val)
        else:
            right = False

        return left or right

    return dfs(root, s)


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        print(currentLevel)
        result.append(currentLevel)

    return result


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    traverse(root)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
