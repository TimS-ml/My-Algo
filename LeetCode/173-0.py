'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

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
