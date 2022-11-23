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
    ans = []

    reverse = 1
    while que:
        size = len(que)
        currLv = deque([])
        for _ in range(size):
            node = que.popleft()
            if reverse == 1:
                currLv.append(node.val)
            else:
                currLv.appendleft(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        reverse *= -1
        ans.append(currLv)
    return ans



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
