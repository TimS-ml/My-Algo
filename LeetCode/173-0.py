'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []  # include the start of every in-order traversal
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        ans = self.stack.pop()
        curr = ans.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def hasNext(self):
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
