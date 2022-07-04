'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    que = deque([root])
    ans = deque([])
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

        ans.appendleft(currLv)
    return ans 


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
