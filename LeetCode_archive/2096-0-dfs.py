'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[A]
LCA = [1] start or dest
    = [2] node x, start at L, dest at R, or reverse

[B]
find path => 'LR' string
if [A.1], no overlap
if [A.2], overlap is: root to LCA

[C]
replace startPath with U
combine start and dest
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        startPath, destPath = '', ''

        def helper(node):
            if not node:
                return
            if node.val == startValue:
                nonlocal startPath
                startPath = ''.join(path)
            elif node.val == destValue:
                nonlocal destPath
                destPath = ''.join(path)

            path.append('L')
            helper(node.left)
            path.pop()

            path.append('R')
            helper(node.right)
            path.pop()

        helper(root)

        # remove common ancestor
        p = 0
        while p < len(startPath) and p < len(destPath) and startPath[p] == destPath[p]:
            p += 1

        startPath = 'U' * (len(startPath) - p)
        destPath = destPath[p:]

        return startPath + destPath
