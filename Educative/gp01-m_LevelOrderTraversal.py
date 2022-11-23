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


def traverse(root):
    que = deque([root])
    ans = []
    # visited = [root]

    while que:
        size = len(que)
        currLv = []
        for _ in range(size):
            node = que.popleft()
            currLv.append(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        ans.append(currLv)
    return ans


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
